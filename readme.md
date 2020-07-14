<h1 align="center">IWNC</h1>

<p align="center">
   <a href="https://ubuntu.com/download/server" title="Ubuntu"><img src="https://img.shields.io/badge/Ubuntu%20Server-20.04%2B-orange?style=plastic&logo=ubuntu"></a>
   <a href="https://docs.python.org/3/" title="Python"><img src="https://img.shields.io/badge/Python-3.8%2B-yellow?style=plastic&logo=python"></a>
   <a href="./LICENSE" title="License"><img src="https://img.shields.io/badge/Licence-GNU%203.0-green?style=plastic"></a>
</p>

<p align="center">
  <a href="#Environnement-requis">Environnement requis</a> •
  <a href="#Prérequis">Prérequis</a> •
  <a href="#Fonctionnement">Fonctionnement</a> •
  <a href="#Liste-des-sondes">Liste des sondes</a> •
  <a href="#Licence">Licence</a>
</p>

Le but de ce projet est d'installer automatiquement wordpress et nagios-core.
Il permet aussi de rajouter une [liste personnalisée de sondes](#Liste-des-sondes) à nagios

## Environnement requis
Pour lancer ce script vous aurez besoin de **Ubuntu Server 20.04+** et **Python 3.8+**

## Prérequis

Installer **python3-pip** pour pouvoir télécharger les modules nécessaires au fonctionnement du script
```
apt-get install pyhton3-pip
```

Installer les modules nécessaires au fonctionnement du script
```
python3 -m pip install wget mysql.connector progress selenium termcolor
```

## Fonctionnement

```
sudo ./iwnc [option]
```

Ce script a plusieurs options en fonction de ce que vous voulez installer

* -w Installe Wordpress ainsi que sa base de données avec MySQL
* -nc Installe nagios-core et lance ensuite l'option -dp
* -dp Installe les plugins officiel de nagios-core
* -pp Installe des plugins (regarder la liste ci-dessous) ajouter pour la supervision de wordpress et nagios-core

## Liste des sondes

| Sonde                 | Description                                                   |
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

## Version des services installés

| Service       | Version                                                     |
| --------------| ------------------------------------------------------------- |
| Wordpress     | <a href="" title="Wordpress"><img src="https://img.shields.io/badge/verison-5.4.2-blue?style=plastic&logo=wordpress"></a>                                                     |
| Nagios-core   | <a href="" title="Nagios-Core"><img src="https://img.shields.io/badge/version-4.4.5-brightgreen?style=plastic"></a>                                |
| Nagios-plugin | <a href="" title="Nagios-Plugin"><img src="https://img.shields.io/badge/version-2.3.3-brightgreen?style=plastic"></a>      |

## Liste des fonctions

* [iwnc.py](./iwnc.py)

    * close_log(msg_nb): ferme le fichier de log avec un message d'erreur ou de succès en fonction de la variable "msg_nb"

    * launch(cmd, msg, err_msg): lance une commande system avec subprocess et print "msg" en cas de succès et "err_msg" en cas d'erreur

    * clean_folder(): nettoie les potentiels fichiers temporaires

    * apt_get(pkg_name_list): utilise apt pour télécharger et installer la liste de paquets "pkg_name_list"

    * wgetfunct(url, dest_path, name): utilise wget pour télécharger "url" vers "dest_path" et qui a pour nom "name"

    * file_search(file, chaine): permet de chercher si un plugin de nagios "chaine" est déjà défini dans le fichier de configuration "file"

    * add_cmd_nagios(name1, cmd1, name2, cmd2): ajoute dans le fichier command.cfg le plugin "name1" avec pour commande "cmd1" et dans le fichier localhost.cfg ajoute le plugin "name2 avec pour commande "cmd2"

    * get_geckodriver(): permet de télécharger geckodriver pour le bon fonctionnement de selenium

* [wordpress.py](./wordpress.py)

    * inst_word(): lance le script d'installation de wordpress

* [nagios.py](./nagios.py)

    * inst_nagios_core(): lance le script d'installation de nagios-Core

    * inst_nagios_plugin(): lance le script d'installation de nagios-core-plugins

* [customPluginNagios.py](./customPluginNagios.py)

    * add_plugin_nagioscore(): lance le script d'installation des plugins personnalisés de nagios core

## Auteur
Arnaud Brison - Openclassroom

## Licence
Ce projet est sous licence GPL - regarder le fichier [LICENSE](./LICENSE) pour plus de details
