
## Description du contenu du r�pertoire

Ce r�pertoire contient les fichiers qui permettent de cr�er les services li�s � la Cartographie (carte et sankey) et au tableau de la quantit� de GES en fonction du mode de transport et de la distance pour une personne.  

- Le fichier calcul.py contient les fonctions calculant la quantit� de GES rejet� sur un trajet. Ces fonctions s'utilisent en indiquant la distance parcourue en km. Le r�sultat est donn�e en kgCO2e.  
- Le fichier main.py contient les services (endpoint) permettant de faire des agr�gations n�cessaires � l'affichage de la carte, du sankey et du tableau.  
Pour lancer l'API, il faut que le jeu de donn�es se situe au m�me endroit que les fichiers main.py et calcul.py. Pour lancer le serveur Fast API, les commandes sont �crites dans la branche "Fast_API" du d�p�t.  
Notons :


**FastAPI** est un framework web haute performance, open source, permettant de cr�er des APIs avec    
Python � partir de la version 3.6          

**Pr�requis :**          
Installer  python          

**D�marche mise en place :**         
1.	Se placer dans un terminal et ex�cuter les commande suivantes :    

    - **pip install fastapi** : permet d'installer FastAPI   
    - **pip install uvicorn** : permet le lancer le serveur API en local   

2.	Cr�er ensuite son r�pertoire de travail et y ajouter un fichier .py dans le lequel le code python sera �crit  
Un exemple de fichier  **''main.py ''** contenant le code pour importer FastAPI et cr�er une route pour  obtenir nos donn�es au format .json  depuis notre serveur API sera joint � ce document.  

3.	Se placer ensuite dans le r�pertoire de travail et lancer la commande suivante pour lancer le serveur FastAPI en local :  
**uvicorn main:app --reload**      
       On peut avoir une erreur de reconnaissance de la commande uvicorn par le terminal si on                  effectue l'installation sur windows, dans ce cas utiliser la commande :  
              **python -m uvicorn main:app --reload**  
        ou travailler dans un environnement de travail python :         
              &nbsp; &nbsp; - **python -m venv venv** : permet de cr�er un environnement de travail virtuel nomm� venv   
              &nbsp; &nbsp; - **venv\Scripts\activate** : permet d'activer l'environnement de travail virtuel   
              &nbsp; &nbsp; - **deactivate** :  permet de d�sactiver l'environnement de travail   
        l'environnement de travail permet �galement d'�viter de t�l�charger les modules n�cessaires     
        pour un projet directement sur son PC   

Le lien du serveur local sur lequel l'API est lancer est ensuite fourni : http://127.0.0.1:8000   


**A savoir :**   
http://127.0.0.1:8000/docs permet d'avoir de la documentation sur notre API 