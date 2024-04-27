from datetime import date
import urllib.request
from urllib.parse import urlparse
import os
import csv
import requests
from bs4 import BeautifulSoup

def book_categories(url_home): # utilisée 1fois, on recupère les adresses mères de chaque catégorie

    response = requests.get(url_home)
    if response.ok:
        soup = BeautifulSoup(response.text, 'lxml')
        urls_categories = []
        for categ_tag in soup.find('ul', {'class': 'nav nav-list'}).findAll('a'):
            urls_categories.append('http://books.toscrape.com/' + categ_tag.get('href'))
        return urls_categories
        print("url des catégories récupérées")
    else:
        print("Veuillez vérifier la connexion ou l'installation de l'environnement, code erreur : ", reponse)

def pages_categorie(url_categorie): #on récupère les liens de chaque livre dans toutes les pages d'une catégorie
    i = 1
    liens_livres_cat = []
    while True:
        response = requests.get(url_categorie)
        soup = BeautifulSoup(response.text, 'lxml')
        # on récupère le bouts d'url spécifique à chaque livre et recompose/ajoute
        # les adresses des livres de la catégorie dans liens_livres_cat
        h3s = soup.find_all('h3')
        for h3 in h3s:
            str_lien_livre = h3.find('a')['href']
            liens_livres_cat.append('http://books.toscrape.com/catalogue/' + str_lien_livre[6:].replace("../", ""))
        try:
            next_btn = soup.find('li', {'class':'next'}).find('a').text
            if next_btn is None:
                return(liens_livres_cat)
                print(f"urls des livres de {url_categorie} page {i} récupérées")
        except:
            return(liens_livres_cat)
        #on itère le numéro de page tant que le bouton 'next' existe
        i += 1
        url_categorie = (url_categorie[:-10] + 'page-' + str(i) + '.html')    

def infos_livres_cat_csv(liens_livres_cat): # pour une catégorie on crée un repertoire on y met les datas dans un csv et les images en .jpg
    # on prépare le répertoire d'accueil de la catégorie
    url_cat_scrap = urlparse(url_categorie)
    parts_categorie = url_cat_scrap.path.strip('/').split('/')[3].split('_')
    categorie_ordre = (parts_categorie[1] + '_' + parts_categorie[0])
    print(f'le dossier portera le nom de {categorie_ordre}')
    # on crée le dossier de catégorie dans lequel seront créés téléchargés les csv jpg de cette catégorie
    os.makedirs(os.path.join(os.getcwd(), os.path.join('Catalogue' + f'_{year}.{month}.{day}_v{i}'), categorie_ordre), exist_ok=False)
    # on se met de côté la variable dossier_categorie pour la destination des fichiers
    dir_cat = os.path.join(os.getcwd(), os.path.join('Catalogue' + f'_{year}.{month}.{day}_v{i}'), categorie_ordre)
            
    for url_livre in liens_livres_cat:
        reponse = requests.get(url_livre)
        soup = BeautifulSoup(reponse.text.encode('latin1').decode('utf-8'), 'lxml')
        # datas à scraper par livre :
        url_livre = url_livre + " "
        table_tds = soup.findAll('td') #tableau avec 4datas en lignes[0:6] UPC,...,prix,prix+taxe,...,dispos
        prod_disponibles = table_tds[5].text
        titre_h = soup.find('h1')
        prod_description = soup.find('article', {'class': 'product_page'}).findAllNext('p')[3].contents[0]
        categorie = soup.find('ul', {'class': 'breadcrumb'}).findAll('li')[2].find('a')
        etoiles = soup.find('div', {'class': 'col-sm-6 product_main'}).findAll('p')[2].attrs['class']
        img_couverture = soup.find('div', {'class': 'item active'}).find('img').attrs['src']
        
        datas = [url_livre, table_tds[0].text, titre_h.text, table_tds[3].text[1:],
         table_tds[2].text[1:], prod_disponibles[10:-11], str(prod_description[:-8]), categorie.text,
         etoiles[1], 'http://books.toscrape.com/' + str(img_couverture)[6:]]
        champs_datas = ['product_page_url', 'universal_product_code(UPC)', 'title',
         'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description',
         'category', 'review_rating', 'image_url']
        # datas[0] = url_livre.append(" ")
        # A la première écriture du fichier "categoroie".csv, on inscrit les champs_datas en header et les datas du 1er livre en dessous
        if not os.path.exists(os.path.join(dir_cat, f"{datas[7]}.csv")):
            with open(os.path.join(dir_cat, f"{datas[7]}.csv"), 'w', encoding='utf8', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(champs_datas)
        # si le fichier csv existe déjà (livre n° >= 2), on ajoute les données en dessous dans le csv
        with open(os.path.join(dir_cat, f"{datas[7]}.csv"), 'a', encoding='utf8', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(datas)
        print(f"datas de '{datas[2]}' de la catégorie '{datas[7]}' écrites avec succès dans {datas[7]}.csv")
        nom_fichier_image = datas[2]
        for char in ':/*?"<>|':
            nom_fichier_image = nom_fichier_image.replace(char, '')
        urllib.request.urlretrieve(f"{datas[-1]}", os.path.join(dir_cat, f"{nom_fichier_image}.jpg"))
        print(f"image de {datas[2]} sauvegardée avec succès dans {nom_fichier_image}.jpg")

url_home = 'http://books.toscrape.com/index.html'
urls_categories = book_categories(url_home)
# on est quand ?
today = date.today()
year, month, day = map(str, (today.year, today.month, today.day))
i = 0
# dossier_courant = os.getcwd(), on ajoute Catalogue et AnnéeMoisJourVersion{i}
# on cherche le prochain i dispo à l'écriture du dossier de sauvegarde par run du programme
while os.path.exists(os.path.join(os.getcwd(), os.path.join('Catalogue' + f'_{year}.{month}.{day}_v{i}'))):
    i += 1
# on créer le dossier pour ce téléchargement
os.makedirs(os.path.join(os.getcwd(), os.path.join('Catalogue' + f'_{year}.{month}.{day}_v{i}')), exist_ok=False)
# on travaillera dans catalog_dir pour toute la session
catalog_dir = os.path.join(os.getcwd(), os.path.join('Catalogue' + f'_{year}.{month}.{day}_v{i}'))
print(f'vos répertoires et fichiers seront dans l\'arborescence du répertoire {catalog_dir}\\')

for url_categorie in urls_categories[1:]:
    liens_livres_cat = pages_categorie(url_categorie)
    infos_livres_cat_csv(liens_livres_cat)
    print(f'la/les pages {url_categorie} ont été sauvegardées dans un csv avec les images des livres')