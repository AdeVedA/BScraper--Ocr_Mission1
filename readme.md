# BScraper - OCR_Mission[1]
------------------------------------------
## - Scraping de librairie en ligne "à la BeautifulSoup" -

##### "Un Scraper sachant scraper sans Scrapy doit BeautifulSouper sans peur ni sans sampler..."
------------------------------------------
BScraper est un programme de scraping récupérant des datas sur un site de vente en ligne de livres http://books.toscrape.com/

1. il crée un dossier catalogue unique au nom daté

2. il télécharge les liens des catégories

3. il récupère les urls des livres en explorant les pages possibles d'une catégorie

4. il itère pour chaque catégorie (avec fonctions distinctes) la suite :

- a. création d'un dossier au nom réordonné \2_travel \3_mystery
pour visualiser les répertoires des catégories selon books.toscrape

- b. il itère pour chaque livre de cette catégorie et remplit ce dossier de :

- - b1. récupération/ajout des datas dans le .csv de la catégorie 

- - b2. téléchargement de l'image du livre en .jpg nommé selon son titre.


------------------------------------------

## I - Setup windows (si python 3.6+ n'est pas installé, commencez par l'annexe A)

  #### A- Créez un repertoire pour le programme
dans votre explorateur windows (WIN+E) 

créez un répertoire (CTRL+MAJ+N) pour le programme où vous le souhaitez et **nommez-le**

ex. : vous pouvez l'appeler BScraper dans d:\chemin\vers\mon\dossier\BScraper

double-cliquez sur le répertoire créé (pour être dedans).

  #### B- lancez l'interpréteur de commande windows
clic gauche dans la barre d'adresse de l'explorateur, écrivez **"cmd"** (à la place de l'adresse)
et appuyez sur **"entrée"** :

	cmd
	
  #### C- clonez le repo Github du projet
dans l'invite de commande (qui indique que vous êtes à l'adresse du dossier créé), tapez:

	git clone https://github.com/AdeVedA/BScraper--Ocr_Mission1.git
 
## II - Configuration

  #### - pour installer un environnement virtuel dans un dossier 'env' du projet, dans l'invite de commande, tapez :
	
	python -m venv env
 
  #### - pour activer l'environnement virtuel créé précédemment, tapez :
	
	env\Scripts\activate.bat
 
  #### - pour y installer les librairies requises, tapez :
	
	pip install -r requirements.txt

  #### - pour désactiver l'environnement virtuel, tapez :

	deactivate

  ##### Bravo on a fini la préparation de l'environnement ! normalement on n'y touche plus !
	
## III - Lancement du programme

	python BScraper.py

## IV - informations sur la structure de données

   les données sont toutes rassemblées et créées (en .csv) ou téléchargées (en .jpg) 
dans les sous-répertoires des catégories des livres (2_travel, 3_mystery, 4_...)
qui sont dans le répertoire Catalogue_2024425_v0 (versionné v1 v2... à chaque lancement du programme).
Nous avons donc en sortie de run l'architecture de répertoire par catégorie suivante :

      racine_projet/

      	    ├───Catalogue_2024.04.15_v0/
      	    |                          ├────2_travel/
      	    |                          |            ├─────travel.csv
      	    |                          |            ├─────bookname1.jpg
      	    |                          |            ├─────bookname2.jpg
      	    |                          |            └─────...
      	    |                          ├────3_mystery/
      	    |                          ├────51_crime/
      	    |                          └────x_nouveau/...
      	    └───Catalogue_2024.04.30_v1/...


# Annexe A - installation de python

Si vous n'avez pas installé Python, téléchargez-la dernière version (ou 3.6+ minimum) sur **"https://www.python.org/downloads/"** et installez-le en vous assurant que **"Add to PATH"** est coché (laissez les autres choix par défaut)
	
