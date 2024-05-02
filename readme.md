# BScraper - OCR_Mission[1]
------------------------------------------
## - Scraping de librairie en ligne "à la BeautifulSoup" -

##### "Un Scraper sachant scraper sans Scrapy doit BeautifulSouper sans peur ni sans sampler..."
------------------------------------------
------------------------------------------
BScraper est un programme de scraping récupérant des datas sur un site de vente en ligne de livres http://books.toscrape.com/

1. il crée un dossier catalogue versionné catalogue_v0 , v1...

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

  #### A- Créez un repertoire pour le programme
lancez votre explorateur windows (WIN+E) 
créez un répertoire (CTRL+MAJ+N) pour le programme où vous le souhaitez et **nommez-le**
ex. : vous pouvez l'appeler **BScraper** dans d:\chemin\vers\mon\dossier\BScraper
**double-cliquez** sur le répertoire créé (pour être dedans).

**NOUVEAU !!!** Option ***rapide et simple*** : 
- téléchargez le fichier Installauto.bat dans votre répertoire et vous le lancez. Si vous avez déjà Git et Python, il installera le programme, l'environnement virtuel, l'activera, y installera les librairies requises.
- téléchargez le fichier Runauto.bat dans votre répertoire et vous le lancez. Il lancera le programme BScraperV2 automatiquement en ayant activé l'environnement virtuel.

sinon, suivez les étapes suivantes :

  #### B- lancez l'interpréteur de commande windows
clic gauche dans la barre d'adresse de l'explorateur, écrivez **"cmd"** (à la place de l'adresse)
et appuyez sur **"entrée"** :

	cmd

nous utiliserons la ligne de commande jusqu'au lancement du programme inclus
	
  #### C- clonez le repo Github du projet dans ce repertoire
dans l'invite de commande (qui indique que vous êtes à l'adresse du dossier créé), tapez tour à tour:

	git init

	git remote add origin git@github.com:AdeVedA/BScraper--Ocr_Mission1.git

	git pull origin BScraperv2

## II - Configuration

  #### - installez un environnement virtuel dans un dossier 'env' du projet, toujours par l'invite de commande :
	
	python -m venv env
 
  #### - activez l'environnement virtuel créé précédemment :
	
	env\Scripts\activate.bat
 
  #### - installez les librairies requises :
	
	pip install -r requirements.txt

  ##### Bravo on a fini la préparation de l'environnement ! normalement on n'y touche plus !
	
## III - Lancement du programme

	python BScraperV2.py

## IV - informations sur la structure de données

les données sont toutes transformées/rassemblées et créées (en .csv) ou téléchargées (en .jpg) dans les sous-répertoires des catégories des livres (2_travel, 3_mystery, 4_...) qui sont dans le répertoire Catalogue_v0 (versionné v1 v2... à chaque lancement du programme).
Nous avons donc en sortie de run l'architecture de répertoires par catégorie suivante :

	racine_projet/
	      	    ├───Catalogue_v0/
	      	    |               ├────2_travel/
	      	    |               |            ├─────travel.csv
	      	    |               |            └─────images/
	      	    |               |            	     ├─────book-name-1.jpg
	      	    |               |            	     └─────book-name-2.jpg...
	      	    |               ├────3_mystery/
	      	    |               ├────51_crime/
	      	    |               └────x_new/...
	      	    └───Catalogue_v1/...

# Annexe 1 - installation de Python & Git

- Si vous n'avez pas installé Python --> **[python](https://www.python.org/downloads/)** et installez-le en vous assurant que ***"Add to PATH"*** est coché (laissez les autres choix par défaut)

- Si vous n'avez pas installé Git  ---> **[Git](https://github.com/git-for-windows/git/releases/download/v2.45.0.windows.1/Git-2.45.0-64-bit.exe)**
