# Projet 4 OPENCLASSROOMS - Développez un programme logiciel en Python

## Téléchargement et installation du programme

### Téléchargement du programme
Depuis l'invite de commande ou le terminal, tapez la commande suivante :

` $ git clone https://github.com/Babel404/P4-Openclassrooms.git `

Rendez-vous ensuite dans le dossier concerné :

` $ cd P4_COUPARD_Bastien`

### Installation de l'environnement virtuel et des packages
Dans le dossier du programme, installez venv en tapant ceci :

` $ python -m venv env`

Puis 

` $ source env/Scripts/activate`

Installez ensuite les requirements :

` $ pip install -r requirements.txt`


Votre programme est prêt à fonctionner !


### Démarrage du programme et fonctionnement

#### Démarrage du programme 

Assurez-vous d'être dans le dossier racine du programme puis tapez la commande suivante :

` $ python ChessTournamentManager.py`

#### Fonctionnement du Programme

Lors du démarrage du programme vous avez accès au menu principal qui se compose de :

- Une interface de création et de modification de Joueur (choix 1)
- Une interface de création de Tournoi (choix 2)
- Une interface pour générer et jouer les matchs d'un tournoi (choix 3'
- Une interface pour générer des rapports (choix 4)

Note : Dans n'importe quel menu il est possible de revenir en arrière ou de fermer le programme en tapant 9

#### Interface de Création et de Modifications de Joueurs

Dans cette interface, vous pouvez créer un joueur, modifier son classement et retrouver l'ID d'un joueur et renseignant son nom et son prénom.

Lors de la création d'un joueur, un ID unique sera automatiquement généré et indiqué à la fin de la création du joueur

Dans le cas où vous accèderiez à un sous-menu par erreur, tapez 0 pour revenir dans l'interface Joueur


#### Interface de Création d'un nouveau Tournoi

Vous pouvez ici créer un nouveau Tournoi en y renseignant les informations demandées.

Un ID unique sera alors automatiquement généré et vous sera communiqué à la fin de la création du tournoi

Vous devez OBLIGATOIREMENT insérer 8 joueurs dans le tournoi afin de pouvoir le créer, pour cela vous pourrez :
- Ajouter des joueurs manuellement un par un (en créant un nouveau joueur ou en y ajoutant un via son ID)
- Ajouter des joueurs automatiquement (Uniquement prévu dans la version DEMO)

#### Démarrer ou Continuer un tournoi

Ce menu sert à générer et à joueur des matchs d'un tournoi choisi.

Lors de l'accès à ce menu, il vous sera demandé l'ID du tournoi, veuillez le noter au préalable.

Le programme détectera automatiquement quel round doit être joué, il générera les 4 matchs et vous donnera accès immédiatement à la génération des scores. Il ne vous restera plus qu'à renseinger ceux-ci afin de terminer le round.

Vous pouvez de ce fait jouer les round un par un à votre rythme.


#### Interface de Rapports

Vous aurez la possibilité de réaliser plusieurs types de rapports :

Concernant les joueurs :
- Afficher tous les joueurs présents dans la base de données par ordre alphabétique
- Afficher tous les joueurs présents dans la base de données par ordre de classement (du plus élevé au plus bas)

Concernant les tournois :
- Afficher tous les tournois présents dans la base de données
- Afficher tous les matchs d'un tournoi, par round
- Afficher tous les matchs d'un tournoi sans distinction du numéro de round

### Rapports flake8

Il est possible de réaliser un rapport flake8 avec de confirmer que le code réponds bien aux standards PEP8, pour cela rendez-vous dans le dossier racine et tapez :

` $ flake8 --format=html --htmldir=flake8_report`

Rendez-vous ensuite dans le dossier flake8_report :

` $ cd flake8_report`

Puis exécutez le script html :

` $ cat index.html`

Le terminal affichera le rapport, vous pouvez ouvrir votre fichier index.html directement depuis un navigateur

