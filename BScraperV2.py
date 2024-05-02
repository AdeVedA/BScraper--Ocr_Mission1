import os
import requests
from bs4 import BeautifulSoup
import csv


def book_categories(url_home):
    # à partir de l'url_home récupèrer les adresses mères
    # de chaque catégorie dans url categorie
    response = requests.get(url_home)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')
        urls_categories  = [f"{url_home}{categ_tag.get('href')}" 
                            for categ_tag in soup.find("ul", {"class": "nav nav-list"}).find_all("a")]
    else:
        print(f"Veuillez vérifier la connexion (à {url_home}) ou l'installation de l'environnement puis relancer le programme, code erreur : {response.status_code}")
        sys.exit()
    return urls_categories

def foldering_catalog():
    # on crée un dossier catalogue incrémenté dans lequel le run inscrira les datas
    i = 0
    while os.path.exists(os.path.join(os.getcwd(), f"Catalogue_v{i}")):
        i += 1
    catalog_folder = os.path.join(os.getcwd(), f"Catalogue_v{i}")
    os.makedirs(catalog_folder, exist_ok=False)
    return catalog_folder

def books_cat_explorer(url_category):
    """ input = page d'accueil de la catégorie, on récupère les urls
    de chaque livre (sortie = liste [allbooks_urls_cat]) dans TOUTES les pages possibles
    d'une catégorie avec iteration sur numéro de pages tant que bouton 'next' existe
    """
    i = 1
    allbooks_urls_cat = []
    while True:
        response = requests.get(url_category)
        soup = BeautifulSoup(response.text, 'lxml')
        for h3 in soup.find_all('h3'):
            allbooks_urls_cat.append('http://books.toscrape.com/catalogue/' 
            + h3.find('a')['href'][6:].replace("../", ""))
        try:
            next_btn = soup.find('li', {'class':'next'}).find('a').text
            if next_btn is None:
                return allbooks_urls_cat
        except:
            return allbooks_urls_cat
        i += 1
        url_category = (url_category[:-10] + 'page-' + str(i) + '.html')
    

def foldering_xcategory(url_category,catalog_folder):
    """ on extrait d'url-category 'travel_2' et en transforme le nom
    pour créer un repertoire catégorie du type '2_travel'
    on crée aussi un répertoire "images" dans le répertoire catégorie
    """
    parts_category_x = url_category.split('/')[6].split('_')
    # x_category = f"{parts_category_x[1]}_{parts_category_x[0]}"
    categ_folder = os.path.join(catalog_folder, f"{parts_category_x[1]}_{parts_category_x[0]}")
    os.makedirs(categ_folder, exist_ok=False)
    images_folder = os.path.join(categ_folder, "images")
    os.makedirs(images_folder, exist_ok=False)
    return categ_folder,images_folder

def csv_file_init(categ_folder):
    # création du .CSV d'une catégorie et écriture des datas_headers en en-tête
    datas_headers = [
        'product_page_url', 'universal_product_code(UPC)', 'title',
         '£_price_including_tax', '£_price_excluding_tax', 'number_available',
          'product_description', 'category', 'review_rating',
           'image_url'
           ]
    with open(os.path.join(categ_folder, f"{categ_folder.split('\\')[6].split('_')[1]}.csv"), 'w',
                 encoding='utf8', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(datas_headers)

def getdatas_book (book_url):
    # on récupère toutes les datas=[] d'un livre
    reponse = requests.get(book_url)
    soup = BeautifulSoup(reponse.text.encode('latin1').decode('utf-8'), 'lxml')
    book_url = book_url + " "
    table_tds = soup.findAll('td') 
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
    return datas

def write_csv_img(datas,images_folder,book_url):
    # ajout des datas de chaque livre de la catégorie dans le CSV de la categorie
    with open(os.path.join(categ_folder, f"{categ_folder.split('\\')[6].split('_')[1]}.csv"), 'a',
             encoding='utf8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(datas)
    # sauvegarder l'IMAGE nommée à partir du nom du livre dans l'url
    with open(os.path.join(images_folder, f"{book_url.rsplit("/", 2)[-2].rsplit("_", 1)[0]}.jpg"), 'wb') as img_f:
        img_data = requests.get(f"{datas[-1]}").content
        img_f.write(img_data)


url_home = 'http://books.toscrape.com/'
urls_categories = book_categories(url_home)
catalog_folder = foldering_catalog()
# deux boucles 'for' pour télécharger
# dans chaque catégorie(ses livres=allbooks_urls_cat) chaque livre(datas)
for url_category in urls_categories[1:]:
    allbooks_urls_cat = books_cat_explorer(url_category)
    categ_folder,images_folder = foldering_xcategory(url_category,catalog_folder)
    csv_file_init(categ_folder)
    for book_url in allbooks_urls_cat:
        datas = getdatas_book(book_url)
        write_csv_img(datas,images_folder,book_url)
    print(f'images & datas des livres de la catégorie " {url_category.split('/')[6].split('_')[0]} " sauvegardées avec succès')
print(f'le BScraping de books.toscrape.com est terminé, bonne journée !')
