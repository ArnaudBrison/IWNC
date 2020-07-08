Titre du projet
Installation automatique de wordpress et nagios-core. Permet aussi de rejouter une liste personnaise de sonde a nagios

Pour commencer
Pour lancer ce script vous aurais besoin de ubuntu 20.04+ et python 3.8+

Prérequis

Installer python3-pip pour pouvoir télécharger les modules nécessaire au fonctionnement du script
```
apt-get install pyhton3-pip
```

Installer les modules nécessaire au fonctionnement du script
```
python3 -m pip install wget mysql.connector progress selenium
```

Fonctionnement
Ce script as plusieurs option en fonction de ce que vous voulais installer

-w Installe Wordpress ansi que sa base de donnée avec MySQL
-nc Installe nagios-core et lance ensuite l'option -dp
-dp Installe les plugin par default de nagios-com
-pp Installe des plugins (regarder la liste ci-dessous) ajouter pour la supervision de wordpress et nagios-core
Liste des sondes :

check_ddos : Verifie si une attaque ddos est  en cours vers le serveur
check_service: Verfie l'etat de nagios-core
check_website_speed: Verifie le temps de reponse du site-web wordpress
check_wp_version: Verifie si des mise a jours sont disponible pour wordpress
check_url_status: Verfie que le site-web wordpress est bien accesible
check_mysql: Verifie l'etat de la base de donnée wordpress

Auteur
Arnaud Brison - openclassroom

Licence
Ce projet est sous licence GPL - regarder le fichier LICENCE.md pour plus de details
