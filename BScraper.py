from datetime import date
import urllib.request
from urllib.parse import urlparse
import os
import csv
import requests
from bs4 import BeautifulSoup

def book_categories(url_home): 
# utilisée 1fois, on recupère les adresses mères de chaque catégorie

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

def livres_pages_categorie(url_categorie):

    # input la page d'accueil de la catégorie, 
    # on récupère les liens de chaque livre 
    # dans TOUTES les pages possibles d'une catégorie

    i = 1
    liens_livres_cat = []
    while True:
        response = requests.get(url_categorie)
        soup = BeautifulSoup(response.text, 'lxml')
        # on récupère le bouts d'url spécifique à chaque livre et recompose/ajoute
        # les adresses des livres de la catégorie dans liens_livres_cat

        # on recrée tous les liens de catégorie à partir de balise html
        for h3 in soup.find_all('h3'):
            liens_livres_cat.append('http://books.toscrape.com/catalogue/' + h3.find('a')['href'][6:].replace("../", ""))
        # et tant que le bouton 'next' existe,
        try:
            next_btn = soup.find('li', {'class':'next'}).find('a').text
            if next_btn is None:
                return(liens_livres_cat)
                print(f"urls des livres de {url_categorie} page {i} récupérées")
        except:
            return(liens_livres_cat)
        # on itère sur le numéro de page et on recommence
        i += 1
        url_categorie = (url_categorie[:-10] + 'page-' + str(i) + '.html')

def dossier_cat_csv(url_categorie):
    
    # on crée un repertoire pour une catégorie
# 1. input = url-categorie / url tree parsing / pour recréer un nom ordonné de répertoire "x-catégorie"
    url_cat_scrap = urlparse(url_categorie)
    parts_categorie_x = url_cat_scrap.path.strip('/').split('/')[3].split('_')
    x_categorie = (parts_categorie_x[1] + '_' + parts_categorie_x[0])
    print(f'le dossier portera le nom de {x_categorie}')

    # on se met de côté la variable dir_cat pour la destination des fichiers de la categorie
    dir_cat = os.path.join(catalog_dir, x_categorie)
    # on crée le dossier de catégorie dans lequel seront créés téléchargés les csv jpg de cette catégorie
    os.makedirs(dir_cat, exist_ok=False)
    return(dir_cat)

def getdatas_livre (url_livre):

    # on récupère les datas des livres
# 2. on crée deux listes : catégories et datas et une adresse image          
    reponse = requests.get(url_livre)
    soup = BeautifulSoup(reponse.text.encode('latin1').decode('utf-8'), 'lxml')
# datas à scraper par livre sur sa page url_livre:
    url_livre = url_livre + " "
    # tableau avec 4datas en lignes[0:6] UPC,...,prix,prix+taxe,...,dispos
    table_tds = soup.findAll('td') 
    prod_dispos = table_tds[5].text[10:-11]
    titre_h = soup.find('h1').text
    prod_description = soup.find('article', {'class': 'product_page'}).findAllNext('p')[3].contents[0][:-8]
    categorie = soup.find('ul', {'class': 'breadcrumb'}).findAll('li')[2].find('a').text
    etoiles = soup.find('div', {'class': 'col-sm-6 product_main'}).findAll('p')[2].attrs['class'][1]
    img_couverture = soup.find('div', {'class': 'item active'}).find('img').attrs['src'][6:]
# deux listes de datas : les champs communs et les datas d'un livre 
    champs_datas = ['product_page_url', 'universal_product_code(UPC)', 'title','price_including_tax',
        'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url']
    datas = [url_livre, table_tds[0].text, titre_h, table_tds[3].text[1:],
        table_tds[2].text[1:], prod_dispos, str(prod_description), categorie,
        etoiles, 'http://books.toscrape.com/' + str(img_couverture)]
    return champs_datas, datas

def ecrire_csv_img(champs_datas,datas): # datas dans un csv & img dans le dossier        

# 3. Si c'est la première écriture du fichier de cette 'catégorie'.csv
    # on inscrit les champs_datas en header et les datas du 1er livre en dessous
        if not os.path.exists(os.path.join(dir_cat, f"{datas[7]}.csv")):
            with open(os.path.join(dir_cat, f"{datas[7]}.csv"), 'w', encoding='utf8', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(champs_datas)
    # si le fichier csv existe déjà (livre n° >= 2), on ajoute les données en dessous dans le csv
        with open(os.path.join(dir_cat, f"{datas[7]}.csv"), 'a', encoding='utf8', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(datas)
        print(f"datas de '{datas[2]}' écrites avec succès dans {datas[7]}.csv")

# 4. on va sauvegarder l'image nommée à partir du 
# titre nettoyé de caractères interdits pour filename
        nom_fichier_image = datas[2]
        for char in ':/*?"<>|':
            nom_fichier_image = nom_fichier_image.replace(char, '')
        urllib.request.urlretrieve(f"{datas[-1]}", os.path.join(dir_cat, f"{nom_fichier_image}.jpg"))
        print(f"image sauvegardée avec succès dans {nom_fichier_image}.jpg")


# on prend la date pour créer un dossier catalogue par requête v0 v1 v2... (Catalogue_2024.4.27_v0)
today = date.today()
year, month, day = map(str, (today.year, today.month, today.day))
#initialiser i pour incrémenter si la version i existe
i = 0
# catalog_dir = os.getcwd(), on ajoute 'Catalogue'_Année.Mois.Jour_v{i} : 
# on cherche le prochain i dispo à l'écriture du dossier catalog_dir
while os.path.exists(os.path.join(os.getcwd(), os.path.join('Catalogue' + f'_{year}.{month}.{day}_v{i}'))):
    i += 1
catalog_dir = os.path.join(os.getcwd(), os.path.join('Catalogue' + f'_{year}.{month}.{day}_v{i}'))
# on créer le dossier pour ce téléchargement, on travaillera dans catalog_dir pour toute la session
os.makedirs(catalog_dir, exist_ok=False)
print(f'vos répertoires et fichiers seront dans l\'arborescence du répertoire {catalog_dir}\\')

url_home = 'http://books.toscrape.com/index.html'
urls_categories = book_categories(url_home) # utilisée 1fois, 
# on a recupéré les urls mères de chaque catégorie

for url_categorie in urls_categories[1:]:
    liens_livres_cat = livres_pages_categorie(url_categorie)
    dir_cat = dossier_cat_csv(url_categorie)
    for url_livre in liens_livres_cat:
        champs_datas, datas = getdatas_livre(url_livre)
        ecrire_csv_img(champs_datas, datas)
    print(f'la/les pages {url_categorie} ont été sauvegardées dans un csv avec les images des livres')