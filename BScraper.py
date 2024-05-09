import os
import requests
from bs4 import BeautifulSoup
import csv


def foldering_catalog():
    """ créer un dossier catalogue dans le répertoire courant où le programme est exécuté.

    Returns:
        catalog_folder (str): Chemin d'accès du répertoire catalogue
    """
    catalog_folder = os.path.join(os.getcwd(), f"Catalogue")
    os.makedirs(catalog_folder, exist_ok=True)
    return catalog_folder


def book_categories():
    """ récupèrer les urls des catégories de livre à partir de l'url d'accueil 

    Args:

    Returns:
    """

    url_home = 'http://books.toscrape.com/'
    try: 
        response = requests.get(url_home)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'lxml')
            urls_categories  = [f"{url_home}{categ_tag.get('href')}" 
                                for categ_tag in soup.find("ul", {"class": "nav nav-list"}).find_all("a")]
    except requests.exceptions.RequestException as e:
        print(f"Veuillez vérifier votre connexion internet à {url_home} puis relancer le programme, erreur : {e}")
        print(exit())
    for url_category in urls_categories[1:]:
        categ_folder,images_folder = xcategory_folder_csv(url_category,catalog_folder)
        books_cat_explorer(url_category,categ_folder,images_folder)
        

def xcategory_folder_csv(url_category,catalog_folder):
    """ créer un répertoire catégorie du type '2_travel' et un répertoire "images" dans celui-ci
    création du .CSV d'une catégorie dans son dossier et écriture des datas_headers en en-tête

    Args:
        url_category (str): url de la categorie
        catalog_folder (str): adresse du repertoire catalogue
    
    Returns:
        categ_folder (str): dossier de la catégorie
        images_folder (str): dossier des images de la categorie
    """
    parts_category_x = url_category.split('/')[6].split('_')
    categ_folder = os.path.join(catalog_folder, f"{parts_category_x[1]}_{parts_category_x[0]}")
    os.makedirs(categ_folder, exist_ok=True)
    images_folder = os.path.join(categ_folder, "images")
    os.makedirs(images_folder, exist_ok=True)
    datas_headers = [
        'product_page_url', 'universal_product_code (upc)', 'title',
         'price_including_tax', 'price_excluding_tax', 'number_available',
          'product_description', 'category', 'review_rating',
           'image_url'
           ]
    with open(os.path.join(categ_folder, f"{parts_category_x[0]}.csv"), 'w',
                 encoding='utf8', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(datas_headers)
    return categ_folder,images_folder


def books_cat_explorer(url_category,categ_folder,images_folder):
    """  récupèrer les urls de chaque livre dans TOUTES les pages possibles d'une catégorie

    Args:
        url_category (str): url d'une catégorie
        categ_folder (str): dossier de la catégorie
        images_folder (str): dossier des images de la categorie

    Returns:
    """
    i = 1
    while True:
        response = requests.get(url_category)
        soup = BeautifulSoup(response.text, 'lxml')
        for h3 in soup.find_all('h3'):
            getdatas_book('http://books.toscrape.com/catalogue/' 
            + h3.find('a')['href'][6:].replace("../", ""),categ_folder,images_folder)
        try:
          next_btn = soup.find('li', {'class':'next'}).find('a').text
          i += 1
          url_category = (url_category[:-10] + 'page-' + str(i) + '.html')
        except AttributeError:
            print(f'images & datas des livres de la catégorie " {url_category.split('/')[6].split('_')[0]} " sauvegardées avec succès')
            break
                 

def getdatas_book (book_url,categ_folder,images_folder):
    """ on récupère toutes les datas=[] d'un livre

    Args:
        book_url (str): url d'un livre

    Returns:
    """
    reponse = requests.get(book_url)
    soup = BeautifulSoup(reponse.text.encode('latin1').decode('utf-8'), 'lxml')
    book_url = book_url + " "
    table_tds = soup.findAll('td') # tableau avec 4datas en lignes[0:6] UPC,...,prix,prix+taxe,...,dispos
    prod_dispos = table_tds[5].text[10:-11]
    titre_h = soup.find('h1').text
    prod_description = soup.find('article', {'class': 'product_page'}).findAllNext('p')[3].contents[0][:-8]   
    categorie = soup.find('ul', {'class': 'breadcrumb'}).findAll('li')[2].find('a').text
    etoiles = soup.find('div', {'class': 'col-sm-6 product_main'}).findAll('p')[2].attrs['class'][1]
    img_couverture = soup.find('div', {'class': 'item active'}).find('img').attrs['src'][6:]

    datas = [
        book_url, table_tds[0].text, titre_h,
         table_tds[3].text[1:], table_tds[2].text[1:], prod_dispos,
          str(prod_description), categorie, etoiles,
           'http://books.toscrape.com/' + str(img_couverture)
           ]
    write_csv_img(book_url,categ_folder,images_folder,datas)


def write_csv_img(book_url,categ_folder,images_folder,datas):
    """ ajout des datas de chaque livre de la catégorie dans le .CSV de la categorie
    puis sauvegarde de l'IMAGE nommée à partir du nom du livre dans l'url

    Args:
        datas (list): liste des datas d'un livre
        images_folder (str): dossier des images de la categorie
        book_url (str): url d'un livre

    Returns:
        .csv et .jpg dans leur répertoire respectif
    """
    with open(os.path.join(categ_folder, f"{categ_folder.split('\\')[6].split('_')[1]}.csv"), 'a',
             encoding='utf8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(datas)
    with open(os.path.join(images_folder, f"{book_url.rsplit("/", 2)[-2].rsplit("_", 1)[0]}.jpg"), 'wb') as img_f:
        img_data = requests.get(f"{datas[-1]}").content
        img_f.write(img_data)


""" on crée le repertoire principal de sauvegarde du catalogue de catégories de livres 
    et on appelle la fonction de récupération des catégories de livre, qui appellera toutes les autres.
"""
catalog_folder = foldering_catalog()
book_categories()
print(f'le BScraping de books.toscrape.com est terminé, bonne journée !')