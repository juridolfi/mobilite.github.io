Etudiante à Polytech Lille en cinquième année en Informatique et Statistique, je suis amenée à réaliser un projet nommé "Projet ingénieur". A l'aide de mon binôme, nous avons travaillé sur les données issues de l'enquête mobilité de l'Université de Lille.   
Ce dépôt nous permet d'afficher le site regroupant les représentations graphiques réalisées lors des sept semaines de projet.   

## Données utilisées

A terme nos graphiques seront utilisées sur les données issues de l'enquête mobilité de 2022 sur les étudiants de l'Université de Lille. Dans le cadre de notre projet, nous avons travaillé dans un premier temps sur un faux jeu de données généré à partir d'un script python. Puis, nous avons utilisé un jeu de données se rapprochant des vraies données. Ce jeu comporte 6 colonnes (variables : Etablissement, Catégorie, Mode, Distance, INSEE_DOM, INSEE_TRA) et 3123 lignes (individus).  

## Description des répertoires

Cette archive contient plusieurs répertoires:

- Le répertoire **Carte** permet de faire l'affichage des flux de déplacement des personnels et étudiants de l'Université. Nous retrouvons dans ce répertoire un fichier index.html qui affiche une carte OpenStreetMap à l'aide de la librairy Leaflet. Le fichier index_sankey.html permet quand à lui d'afficher un graphique de Sankey des flux de déplacement;
- Le répertoire **Client** est composé de fichier html et css qui permettent l'affichage du site. Par exemple, le fichier index.html contient la page d'accueil du site;
- Le répertoire **Graphe_chartjs" permet de faire l'affichage de diagramme en barre et de pie;
- Le répertoire **Tableau** contient les fichiers js et html nécessaire à l'affichage d'un tableau de la quantité des GES annuel en fonction du mode de transport et de la distance parcourue (tranche de distance) pour une personne seule;
- Le répertoire **API** contient API REST utilisé.

## Utilisation API

Nous avons utilisé une API en locale sur une machine pour fournir des données aux graphiques. L'API REST que nous avons utilisé est fastAPI. Les commandes de lancement sont disponibles dans le répertoire **API**.
