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

- a. création d'un dossier de catégorie au nom réordonné \2_travel \3_mystery
	pour ordonner les répertoires des catégories selon books.toscrape et
	création d'un répertoire images dans le répertoire de catégorie.

- b. il itère pour chaque livre de cette catégorie et remplit ce dossier de :

- - b1. récupération/ajout des datas dans le .csv de la catégorie 

- - b2. téléchargement de l'image du livre en .jpg nommé selon son titre dans un répertoire images du dossier catégorie.
------------------------------------------
------------------------------------------
## I - Setup windows

#### ( si [Git](https://github.com/git-for-windows/git/releases/download/v2.45.0.windows.1/Git-2.45.0-64-bit.exe) et [python 3.6+](https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe) ne sont pas installés, commencez par l'annexe 1 !)
------------------------------------------
  #### A - Créez un répertoire pour le programme
Lancez votre explorateur windows (WIN+E) 
Créez un répertoire (CTRL+MAJ+N) pour le programme où vous le souhaitez et **nommez-le**
ex. : vous pouvez l'appeler **BScraper** dans d:\chemin\vers\mon\dossier\BScraper
**double-cliquez** sur le répertoire créé pour aller dedans.

  #### B - lancez l'interpréteur de commande windows
Clic gauche dans la barre d'adresse de l'explorateur, écrivez **"cmd"** (à la place de l'adresse)
et appuyez sur **"entrée"** (comme à chaque instruction en ligne future):

	cmd
	
  #### C - clonez le repo Github du projet dans ce répertoire
dans le terminal (l'invite de commande) qui indique bien que vous êtes à l'adresse du dossier créé, écrivez tour à tour:

	git init

puis : 

	git pull https://github.com/AdeVedA/BScraper--Ocr_Mission1.git -t main

  #### D - installez un environnement virtuel dans un dossier 'env' du projet, toujours par l'invite de commande :
	
	python -m venv env
 
  #### E - activez l'environnement virtuel créé précédemment :
	
	env\Scripts\activate.bat
 
  #### F - installez les librairies requises :
	
	pip install -r requirements.txt

  #### G - Lancement du programme (l'environnement virtuel doit avoir été activé avant):

	python BScraper.py

  #### H - Désactivez l'environnement virtuel

	deactivate
-------------------------
-------------------------

## II - Setup Linux/Mac

#### ( si **[Git](https://sourceforge.net/projects/git-osx-installer/files/git-2.23.0-intel-universal-mavericks.dmg/download?use_mirror=autoselect)** et **[python](https://www.python.org/ftp/python/3.12.3/python-3.12.3-macos11.pkg)** ne sont pas installés, commencez par l'annexe 1 !)

-------------------------
	
  #### A- lancez un terminal

clic sur loupe/recherche lancez

	terminal
	
  #### B - Créez un répertoire pour le programme et placez-vous dedans
  par exemple si vous souhaitez appeler ce dossier "BScraper" :

	mkdir BScraper

puis :

	cd BScraper

  #### C - clonez le repo Github du projet dans ce répertoire
dans le terminal (l'invite de commande) qui indique bien que vous êtes à l'adresse du dossier créé, écrivez tour à tour:

	git init

puis : 

	git pull https://github.com/AdeVedA/BScraper--Ocr_Mission1.git -t main

  #### D - installez un environnement virtuel dans un dossier 'env' du projet, toujours par le terminal :
	
	python3 -m venv env

  #### E - activez l'environnement virtuel créé précédemment :
	
	source env/bin/activate
 
  #### F - installez les librairies requises :
	
	pip install -r requirements.txt

  #### G - Lancement du programme (l'environnement virtuel doit avoir été activé avant):

	python3 BScraper.py

  #### H - Désactivez l'environnement virtuel

	deactivate
 

## III - informations sur la structure de données

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
=======================================================================

pour Windows 64bits :
--------------------

installez **[Git](https://github.com/git-for-windows/git/releases/download/v2.45.0.windows.1/Git-2.45.0-64-bit.exe)** 
verifiez en tapant "cmd" dans le menu démarrer puis "git version" dans le terminal

installez **[python](https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe)** en vous assurant que ***"Add to PATH"*** est coché (laissez les autres choix par défaut)
verifiez en tapant "cmd" dans le menu démarrer puis "python --version" dans le terminal

pour Mac/Linux :
--------------------
**Git**
cliquez sur l'icone de recherche (loupe), écrivez "terminal" (on vérifie si git est déjà présent)

	git version

si ok, passez à python. 
sinon, installez ce qu'il vous propose d'installer ("command line developer tools") puis recommencez "git version" en terminal,
sinon : installez **[Git](https://sourceforge.net/projects/git-osx-installer/files/git-2.23.0-intel-universal-mavericks.dmg/download?use_mirror=autoselect)**
puis revérifiez git version dans le terminal

**Python**
installez **[python](https://www.python.org/ftp/python/3.12.3/python-3.12.3-macos11.pkg)**


