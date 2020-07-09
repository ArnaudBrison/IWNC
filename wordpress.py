from iwnc import apt_get, wgetfunct, launch, clean_folder, close_log, log_file, wordmdp
from os import path
import mysql.connector
from mysql.connector import Error
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from progress.bar import Bar
def inst_word():
	#######INSTALLATION########
	print ('Debut de l\'installation d\'apache, la base de donnee mysql et wordpress', file=log_file)

	#Install package needed for apache
	pkg_name_list = ["apache2", "php7.4", "php7.4-mysql", "libapache2-mod-php7.4", "mysql-server", "firefox"]
	apt_get(pkg_name_list)

	print ('Installation des packet reussie', file=log_file)
	print ('Les log de apt ce trouve dans le fichier restore_apt.log', file=log_file)
	wordpress_tar_path = '/tmp/wordpress.tar.gz'
	if (path.exists('/var/www/html/wordpress') == False):

		#Get the lastest wordpress tar
		url = "https://wordpress.org/latest.tar.gz"
		print ('Telechargement de l\'archive de wordpress', file=log_file)
		wgetfunct(url, wordpress_tar_path, 'wordpress')
		print ('L\'archive a bien ete telecharger', file=log_file)

		#Open archive
		untar_wordpress_tar_cmd = "tar -C /var/www/html -zxf " + wordpress_tar_path
		msg = ('Transfert du contenu de l\'archive dans le dossier /var/www/html/')
		err_msg = ('Le transfert du contenu de l\'archive dans le dossier /var/www/html a echouer')
		launch(untar_wordpress_tar_cmd , msg, err_msg)
	mysqlinst = input('Mysql est deja installer ? (o or n): ')
	if (mysqlinst == 'n'):
		print ('Debut de la configuration de MYSQL')
		mysqlmdp = input("Qu'elle mot de passe souhaiter vous mettre a l\'utilisateur root pour mysql?: ")
		#Change mysql root passwd
		root_mysql_change = "sudo mysql -u root -py -e \'ALTER USER \'root\'@\'localhost\' IDENTIFIED WITH mysql_native_password BY \"" + mysqlmdp + "\"\'"
		msg = ('Changement du mdp root avec succees')
		err_msg = ('Le mdp root n\'a pas put etre changer')
		launch(root_mysql_change, msg, err_msg)
	elif (mysqlinst == 'o'):
		mysqlmdp = input("Veuiller rentrer votre mot de passe pour l' utilisateur root de mysql: ")
		print ('Debut de la configuration de MYSQL')
	wordmdp = input ("Qu'elle mot de passe souhaiter vous mettre a l\'utilisateur wordpress pour mysql?:")

	#Information mysql connection
	ip_address = "localhost";
	user = "root";

	try:
		connection = mysql.connector.connect(host=ip_address, user=user, password=mysqlmdp, auth_plugin='mysql_native_password')

		if connection.is_connected():
			cursor = connection.cursor()
			cursor.execute("CREATE DATABASE wordpress;")
			print ("Creation de la base de donnee wordpress", file=log_file)
			cursor.execute("CREATE USER 'wordpress'@'localhost' IDENTIFIED WITH mysql_native_password BY \'" + wordmdp + "\';")
			print ("Creation de l' utilisateur wordpress", file=log_file)
			cursor.execute("GRANT ALL PRIVILEGES ON wordpress.* TO 'wordpress'@'localhost';")
			cursor.execute("FLUSH PRIVILEGES;")
			print ("Dont des droits sur la base de donnee wordpress a l' utilisateur wordpress", file=log_file)

	except Error as e:
		print('Erreur pendant la connection a MySQL', e, file=log_file)
	finally:
		if (connection.is_connected()):
			cursor.close()
			connection.close()
			print('La connexion a mysql est fermer', file=log_file)
	print('Fin de la configuration de MYSQL')
	print('Debut de la configuration de wordpress')
	bar = Bar('Configuration en cours...', max=4)
	bar.next()
	wordpress_path = "/var/www/html/wordpress/"
	wp_config_create = "cp " + wordpress_path + "wp-config-sample.php " + wordpress_path + "wp-config.php"
	msg = ('Le fichier wp-config.php a ete creer')
	err_msg = ('Le fichier wp-config.phph n\'a pas put etre creer')
	launch(wp_config_create, msg, err_msg)
	bar.next()

	fin = open(wordpress_path + "wp-config.php", "rt")
	data = fin.read()
	data = data.replace('database_name_here', 'wordpress')
	data = data.replace('username_here', 'wordpress')
	data = data.replace('password_here', wordmdp)
	fin.close()
	fin = open(wordpress_path + "wp-config.php", "wt")
	fin.write(data)
	fin.close()
	bar.next()
	print ('Le fichier wp-config.php a ete modifier', file=log_file)

	options = Options()
	options.headless = True

	driver = webdriver.Firefox(options=options)
	driver.get('http://192.168.238.134/wordpress/wp-admin/install.php')

	title = input('\nQu\'elle titre voulais vous mettre a voitre site?:')
	mail = input('Qu\'elle est l\'adresse mail pour l\'administrateur?:')
	weblog_title = driver.find_element_by_id('weblog_title')
	username = driver.find_element_by_id('user_login')
	password = driver.find_element_by_id('pass1')
	passw = password.get_attribute('data-pw')
	email = driver.find_element_by_id('admin_email')
	install_button = driver.find_element_by_id('submit')

	weblog_title.send_keys(title)
	username.send_keys('admin')
	email.send_keys(mail)
	install_button.click()
	bar.next()
	bar.finish()

	print ('Fin de la configuration et de l\'installation de wordpress les identifiant sont lister a la fin du fichier de log')
	print ('Fin de la configuration et de l\'installation de wordpress', file=log_file)
	if (mysqlinst == 'n'):
		print ('Mot de passe root mysql: ', mysqlmdp, file=log_file)
	print ('Mot de passe wordpress mysql:',  wordmdp, file=log_file)
	print ('Identifiant site wordpress: admin', file=log_file)
	print ('Mot de passe du site wordpress:', passw, file=log_file)
	#####FIN INSTALLATION######
