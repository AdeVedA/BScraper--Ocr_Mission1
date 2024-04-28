# BScraper - OCR_Mission[1]
------------------------------------------
## - Scraping de librairie en ligne "à la BeautifulSoup" -

##### "Un Scraper sachant scraper sans Scrapy doit BeautifulSouper sans peur ni sans sampler..."
------------------------------------------
BScraper est un programme de scraping récupérant des datas sur un site de vente en ligne de livres http://books.toscrape.com/

1. il crée un dossier catalogue unique au nom daté

2. il télécharge les liens des catégories

3. il explore la pagination et récupère les urls des livres d'une catégorie

4. j'itère pour chaque catégorie :

- a. création d'un dossier du nom ré-ordonné de la catégorie 

- b. on itère pour chaque livre

- - b1. récupération/ajout des datas dans le csv de la catégorie 

- - b2. téléchargement/sauvegarde de l'image du livre en .jpg nommé selon son titre.


------------------------------------------

## I - Setup windows (si python 3.x n'est pas installé, commencez par l'annexe A)

  #### A- Créez un repertoire pour le programme
dans votre explorateur windows (WIN+E) 

créez un répertoire (CTRL+MAJ+N) pour le programme où vous le souhaitez et **nommez-le**

ex. : vous pouvez l'appeler BScraper dans d:\chemin\vers\mon\dossier\BScraper

double-cliquez sur le répertoire créé (pour être dedans).

  #### B- lancez l'interpréteur de commande windows
clic gauche dans la barre d'adresse de l'explorateur, écrivez **"cmd"** et appuyez sur **"entrée"** :

	cmd
	
  #### C- clonez le repo Github du projet
dans l'invite de commande (qui indique que vous êtes à l'adresse du dossier créé), tapez:

	git clone https://github.com/AdeVedA/BScraper--Ocr_Mission1.git
 
## II - Configuration

  #### - pour installer un environnement virtuel dans un dossier 'env' du projet, dans l'invite de commande, tapez :
	
	python -m venv env
 
  #### - pour activer l'environnement virtuel créé précédemment, tapez :
	
	env\Scripts\activate.bat
 
  #### - pour y installer les librairies, tapez :
	
	pip install -r requirements.txt

  #### - pour désactiver l'environnement virtuel, tapez :

	deactivate
	
  ##### Bravo on a fini la préparation de l'environnement ! normalement on n'y touche plus !
	
## III - Lancement du programme

	python BScraper.py

## IV - informations sur la structure de données

   les données sont toutes rassemblées et créées (en .csv) ou téléchargées (en .jpg) 
dans le sous-répertoire de catégorie du livre (2_travel, 3_mystery, 4_...)
dans le répertoire Catalogue (versionné à chaque lancement du programme)
et une architecture de répertoire par catégorie ensuite :

      racine_projet/

      	    ├───Catalogue_2024.04.15_v0/
      	    |                          ├────2_travel/
      	    |                          |            ├─────travel.csv
      	    |                          |            ├─────bookname1.jpg
      	    |                          |            ├─────bookname2.jpg
      	    |                          |            └─────...
      	    |                          ├────3_mystery/
      	    |                          ├────51_etc/
      	    |                          └────x_etc/
      	    └───Catalogue_2024.04.30_v1/...


***** Annexe A = installation de python

Si vous n'avez pas installé Python, téléchargez-la dernière version sur **"https://www.python.org/downloads/"** et installez-le en vous assurant que **"Add to PATH"** est coché (laissez les autres choix par défaut)
	
