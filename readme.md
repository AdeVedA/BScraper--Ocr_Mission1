# BScraper - OCR_Mission[1]
## - Scraping de librairie en ligne "à la BeautifulSoup" -

#### "Un Scraper sachant scraper sans Scrapy doit BeautifulSouper sans peur ni sans sampler..."
------------------------------------------
Ce repo herberge un programme de scraping réalisé sur demande pour récupérer des datas sur les livres & catégories d'un site de vente en ligne de livres.
Ces datas sont structurées par catégorie de livre, sauvegardées en fichier .csv avec "informations" par livre,
et chaque image de livre est téléchargée en fichier .jpg nommé selon son titre.
Les informations sur l'arborescence d'écriture des données figurent en IV

------------------------------------------

## I - Installation windows (si python 3.x n'est pas installé, commencez par l'annexe A)

  #### A- Créez un repertoire pour le programme
dans votre explorateur windows :
créez un répertoire pour le programme où vous le souhaitez (CTRL+N) **nommez-le** 
(ex. : dossier dans d:\chemin\de\mon\dossier)
double-cliquez sur le répertoire créé pour vous y trouver

  #### B- lancez l'interpréteur de commande windows
clic gauche dans la barre d'adresse de l'explorateur, écrivez **"cmd"** et appuyez sur **"entrée"** :

	cmd
	
  #### C- clonez le repo Github du projet
dans l'invite de commande, écrivez:

	git clone https://github.com/AdeVedA/OCRmission1.git
 
## II - Installation d'un environnement virtuel et lancement du programme

  #### - pour installer un environnement virtuel dans un dossier 'env' du projet, dans l'invite de commande, tapez :
	
	python -m venv env
 
  #### - pour activer l'environnement virtuel créé précédemment, dans l'invite de commande, tapez :
	
	env\Scripts\activate.bat
 
  #### - pour y installer les librairies dans l'invite de commande, tapez :
	
	pip install -r requirements.txt

  ### Bravo on a fini la préparation de l'environnement ! normalement on n'y touche plus !
	
## III - Lancement du programme

	python BScraper_v44.py

## IV - informations sur la structure de données

   les données sont toutes rassemblées et créées (en .csv) ou téléchargées (en .jpg) 
dans un nouveau répertoire versionné à chaque lancement et une architecture de répertoire par catégorie ensuite :

         racine/
      	    |---Catalogue_année.mois.jour_v0/
      	    |                               |----2_travel/
      	    |                               |            |-----travel.csv
      	    |                               |            |-----book1_name.jpg
      	    |                               |            |-----book2_name.jpg
      	    |                               |            |-----...
      	    |                               |----3_mystery/
      	    |                               |----x_etc/
      	    |                               L----51_etc/
      	    L---Catalogue_année.mois.jour_v1/ ...
------------------------------------------
# Annexe A = installation de python

Si vous n'avez pas installé Python, téléchargez-la dernière version sur **"https://www.python.org/downloads/"** et installez-le en vous assurant que **"Add to PATH"** est coché (laissez les autres choix par défaut)
	
