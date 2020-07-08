<h1 align="center">IWNC</h1>

<p align="center">
   <a href="https://docs.python.org/3/" title="Ubuntu"><img src="https://img.shields.io/badge/Ubuntu%20Server-20.04%2B-orange"></a>
   <a href="https://docs.python.org/3/" title="Python"><img src="https://img.shields.io/badge/Python-3.8%2B-yellow"></a>
   <a href="./LICENSE" title="License"><img src="https://img.shields.io/badge/Licence-GNU%203.0-green"></a>
</p>

<p align="center">
  <a href="#Environnement-requis">Environnement requis</a> •
  <a href="#Prérequis">Prérequis</a> •
  <a href="#Fonctionnement">Fonctionnement</a> •
  <a href="#Liste-des-sondes">Liste des sondes</a> •
  <a href="#Licence">Licence</a>
</p>

Le but de ce projet est d'installer automatique wordpress et nagios-core. Permets aussi de rajouter une liste personnalisée de sonde à nagios

## Environnement requis
Pour lancer ce script vous aurais besoin de Ubuntu Server 20.04+ et Python 3.8+

## Prérequis

Installer python3-pip pour pouvoir télécharger les modules nécessaires au fonctionnement du script
```
apt-get install pyhton3-pip
```

Installer les modules nécessaires au fonctionnement du script
```
python3 -m pip install wget mysql.connector progress selenium
```

## Fonctionnement
Ce script a plusieurs options en fonction de ce que vous voulez installer

-w Installe Wordpress ainsi que sa base de données avec MySQL
-nc Installe nagios-core et lance ensuite l'option -dp
-dp Installe les plugins par défaut de nagios-core
-pp Installe des plugins (regarder la liste ci-dessous) ajouter pour la supervision de wordpress et nagios-core

## Liste des sondes

| Nom de la sonde & Lien       | Description                                            |
| --------------------- | ------------------------------------------------------------- |
| [check_ddos]          | Vérifie si une attaque ddos est  en cours vers le serveur.    |
| [check_service]       | Vérifie l'état de nagios-core.                                |
| [check_website_speed] | Vérifie le temps de réponse du site web wordpress.            |
| [check_wp_version]    | Vérifie si des mises à jours sont disponibles pour wordpress. |
| [check_url_status]    | Vérifie que le site-web wordpress est bien accessible.        |
| [check_mysql]         | Vérifie l'état de la base de données wordpress.               |

[check_ddos]: https://exchange.nagios.org/directory/Plugins/Security/check_ddos/details
[check_service]: https://github.com/jonschipp/nagios-plugins
[check_website_speed]: https://exchange.nagios.org/directory/Plugins/Websites%2C-Forms-and-Transactions/Check-Website-Speed/details
[check_wp_version]: https://exchange.nagios.org/directory/Plugins/CMS-and-Blog-Software/Wordpress/check_wp_version/details
[check_url_status]: https://exchange.nagios.org/directory/Plugins/Websites%2C-Forms-and-Transactions/check_url_status/details
[check_mysql]: https://github.com/nagios-plugins/nagios-plugins

## Auteur
Arnaud Brison - Openclassroom

## Licence
Ce projet est sous licence GPL - regarder le fichier [LICENSE](./LICENSE) pour plus de details
