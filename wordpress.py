from main import apt_get, wgetfunct, launch, clean_folder, close_log
from os import path
import mysql.connector
from mysql.connector import Error
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
def inst_word():
	#######INSTALLATION########
	print ('Debut de l\'installation d\'apache, la base de donnee mysql et wordpress')

	#Install package needed for apache
	pkg_name_list = ["apache2", "php7.4", "php7.4-mysql", "libapache2-mod-php7.4", "mysql-server", "firefox"]
	apt_get(pkg_name_list)

	print ('Installation des packet reussie')
	print ('Les log de apt ce trouve dans le fichier restore_apt.log')
	wordpress_tar_path = '/tmp/wordpress.tar.gz'
	if (path.exists('/var/www/html/wordpress') == False):

		#Get the lastest wordpress tar
		url = "https://wordpress.org/latest.tar.gz"
		print ('Telechargement de l\'archive de wordpress')
		wgetfunct(url, wordpress_tar_path, 'wordpress')
		print ('L\'archive a bien ete telecharger')

		#Open archive
		untar_wordpress_tar_cmd = "tar -C /var/www/html -zxf " + wordpress_tar_path
		msg = ('Transfert du contenu de l\'archive dans le dossier /var/www/html/')
		err_msg = ('Le transfert du contenu de l\'archive dans le dossier /var/www/html a echouer')
		launch(untar_wordpress_tar_cmd , msg, err_msg)

	print ('Debut de la mise en place de la base de donnée', file=old_stdout)
	#Change mysql root passwd
	root_mysql_change = "sudo mysql -u root -py -e 'ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY \"Yters3j/fg\"'"
	msg = ('Changement du mdp root avec succees')
	err_msg = ('Le mdp root n\'a pas put etre changer')
	launch(root_mysql_change, msg, err_msg)

	#Information mysql connection
	ip_address = "localhost";
	user = "root";
	passwd = "Yters3j/fg";

	try:
		connection = mysql.connector.connect(host=ip_address, user=user, password=passwd, auth_plugin='mysql_native_password')

		if connection.is_connected():
			cursor = connection.cursor()
			cursor.execute("CREATE DATABASE wordpress;")
			print ("Creation de la base de donnee wordpress")
			cursor.execute("CREATE USER 'wordpress'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Yters3/jfg';")
			print ("Creation de l' utilisateur wordpress")
			cursor.execute("GRANT ALL PRIVILEGES ON wordpress.* TO 'wordpress'@'localhost';")
			cursor.execute("FLUSH PRIVILEGES;")
			print ("Dont des droits sur la base de donnee wordpress a l' utilisateur wordpress")

	except Error as e:
		print('Erreur pendant la connection a MySQL', e)
	finally:
		if (connection.is_connected()):
			cursor.close()
			connection.close()
			print('La connexion a mysql est fermer')
	print ('Fin de la création de la base de donnée', file=old_stdout)
	print ('Debut de la configuration de wordpress', file=old_stdout)
	wordpress_path = "/var/www/html/wordpress/"
	wp_config_create = "cp " + wordpress_path + "wp-config-sample.php " + wordpress_path + "wp-config.php"
	msg = ('Le fichier wp-config.php a ete creer')
	err_msg = ('Le fichier wp-config.phph n\'a pas put etre creer')
	launch(wp_config_create, msg, err_msg)

	fin = open(wordpress_path + "wp-config.php", "rt")
	data = fin.read()
	data = data.replace('database_name_here', 'wordpress')
	data = data.replace('username_here', 'wordpress')
	data = data.replace('password_here', 'Yters3/jfg')
	fin.close()
	fin = open(wordpress_path + "wp-config.php", "wt")
	fin.write(data)
	fin.close()

	options = Options()
	options.headless = True

	print ('fin wp-config change')
	driver = webdriver.Firefox(options=options)
	print ('test')
	driver.get('http://192.168.238.134/wordpress/wp-admin/install.php')

	weblog_title = driver.find_element_by_id('weblog_title')
	username = driver.find_element_by_id('user_login')
	password = driver.find_element_by_id('pass1')
	test = password.get_attribute('data-pw')
	print ('print passw:', test)
	email = driver.find_element_by_id('admin_email')
	install_button = driver.find_element_by_id('submit')

	weblog_title.send_keys('orga.fr')
	username.send_keys('admin')
	email.send_keys('admin@orga.fr')
	install_button.click()

	print ('Fin de l\'installation de wordpress')
	print ('Fin de la configuration de wordpress', file=old_stdout)
	clean_folder()
	close_log('0')
	#####FIN INSTALLATION######
