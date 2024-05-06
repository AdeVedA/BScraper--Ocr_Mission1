# BScraper - OCR_Mission[1]
------------------------------------------
## - Scraping de librairie en ligne "à la BeautifulSoup" -

##### "Un Scraper sachant scraper sans Scrapy doit BeautifulSouper sans peur ni sans sampler..."
------------------------------------------
------------------------------------------
BScraper est un programme de scraping récupérant des datas sur un site de vente en ligne de livres http://books.toscrape.com/

1. il crée un dossier catalogue...

2. il télécharge les liens des catégories

3. il récupère les urls des livres en explorant les pages possibles d'une catégorie

4. il itère pour chaque catégorie (avec fonctions distinctes) la suite :

- a. création d'un dossier au nom réordonné \2_travel \3_mystery
pour ordonner les répertoires des catégories selon books.toscrape

- b. il itère pour chaque livre de cette catégorie et remplit ce dossier de :

- - b1. récupération/ajout des datas dans le .csv de la catégorie 

- - b2. téléchargement de l'image du livre en .jpg nommé selon son titre dans un répertoire images du dossier catégorie.
------------------------------------------
------------------------------------------
## I - Setup windows 
#### ( si [Git](https://github.com/git-for-windows/git/releases/download/v2.45.0.windows.1/Git-2.45.0-64-bit.exe) et [python 3.6+](https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe) ne sont pas installés, commencez par l'annexe 1 !)

  #### A- Créez un répertoire pour le programme
Lancez votre explorateur windows (WIN+E) 
Créez un répertoire (CTRL+MAJ+N) pour le programme où vous le souhaitez et **nommez-le**
ex. : vous pouvez l'appeler **BScraper** dans d:\chemin\vers\mon\dossier\BScraper
**double-cliquez** sur le répertoire créé (pour être dedans - il est vide).

  #### B- lancez l'interpréteur de commande windows
Clic gauche dans la barre d'adresse de l'explorateur, écrivez **"cmd"** (à la place de l'adresse)
et appuyez sur **"entrée"** (comme à chaque instruction en ligne future):

	cmd
	
  #### C- clonez le repo Github du projet dans ce répertoire
dans l'invite de commande (qui indique que vous êtes à l'adresse du dossier créé), écrivez tour à tour:

	git init

puis : 

	git pull https://github.com/AdeVedA/BScraper--Ocr_Mission1.git -t main

  #### D- lancez l'installation et le run automatiques, ou bien passez en II configuration manuelle
pour installer un environnement virtuel, l'activer et lui fournir les librairies nécessaires, lancez 

	installauto.bat

pour activer l'environnement virtuel et lancer le programme de scraping automatiquement, sinon passez en III - lancement du programme

	runauto.bat

## II - Configuration manuelle

  #### a - installez un environnement virtuel dans un dossier 'env' du projet, toujours par l'invite de commande :
	
	python -m venv env
 
  #### b - activez l'environnement virtuel créé précédemment :
	
	env\Scripts\activate.bat
 
  #### c - installez les librairies requises :
	
	pip install -r requirements.txt
	
## III - Lancement manuel du programme (avec environnement virtuel activé, faites II b)

	python BScraper.py

## IV - informations sur la structure de données

les données sont toutes transformées/rassemblées et créées (en .csv) ou téléchargées (en .jpg) dans les sous-répertoires des catégories des livres (2_travel, 3_mystery, 4_...) qui sont dans le répertoire Catalogue.
Nous avons donc en sortie de run l'architecture de répertoires par catégorie suivante :

	racine_projet/
	      	    ├───Catalogue/
	      	                 ├────2_travel/
	      	                 |            ├─────travel.csv
	      	                 |            └─────images/
	      	                 |            	     ├─────book-name-1.jpg
	      	                 |            	     └─────book-name-2.jpg...
	      	                 ├────3_mystery/
	      	                 ├────51_crime/
	      	                 └────x_new/...
	      	    

# Annexe 1 - installation de Python & Git

- Si vous n'avez pas installé Python --> **[python](https://www.python.org/downloads/)** et installez-le en vous assurant que ***"Add to PATH"*** est coché (laissez les autres choix par défaut)

- Si vous n'avez pas installé Git  ---> **[Git](https://github.com/git-for-windows/git/releases/download/v2.45.0.windows.1/Git-2.45.0-64-bit.exe)**
