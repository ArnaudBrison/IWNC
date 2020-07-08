from main import apt_get, wgetfunct, launch, clean_folder, close_log
import pwd
import grp
from os import path

def inst_nagios_core():
	#Install required package
	pkg_name_list = ["apache2", "php", "php-gd",
	"php-imap", "php-curl", "libxml-libxml-perl",
	"libnet-snmp-perl", "libperl-dev", "libnumber-format-perl",
	"libconfig-inifiles-perl", "libdatetime-perl", "libnet-dns-perl",
	"libpng-dev", "libjpeg-dev", "libgd-dev", "gcc", "make", "autoconf", "libc6", "unzip"]
	apt_get(pkg_name_list)

	print ('Debut de la creation et configuration de l\'utilisateur nagios et du groupe nagcmd', file=old_stdout)
	#Create user nagios
	try:
		pwd.getpwnam('nagios')
	except KeyError:
		create_user_nagios = "useradd -m -p $(openssl passwd nagios) nagios --create-home"
		msg = ('Creation de l\'utilisateur nagios')
		err_msg = ('L\'utilisateur nagios n\'a pas put etre creer')
		launch(create_user_nagios , msg, err_msg)

	#Create groupe nagcmd
	try:
		grp.getgrnam('nagcmd')
	except KeyError:
		create_grp_nagcmd = "groupadd nagcmd"
		msg = ('Creation du groupe nagcmd')
		err_msg = ('Le groupe nagcmd n\'a pas put etre creer')
		launch(create_grp_nagcmd , msg, err_msg)

	#add user nagios && www-data to nagcmd groupe
	add_user_grp_nagcmd = "usermod -a -G nagcmd nagios && usermod -a -G nagcmd www-data"
	msg = ('Ajout des utilisateur au groupe nagcmd')
	err_msg = ('L\'Ajout des utilisateur au groupe nagcmd a echouer')
	launch(add_user_grp_nagcmd , msg, err_msg)

	#Edit /etc/passwd file
	fin = open("/etc/passwd", "a+")
	fin.write('nagios:x:1001:1001::/home/nagios:/bin/bash')
	fin.close()

	#Creer le dossier /home/nagios/download
	if (path.exists('/home/nagios/downloads') == False):
		mkdir_downloads_folder = "mkdir /home/nagios/downloads"
		msg = ('Creation du dossier /home/nagios/downloads avec succes')
		err_msg = ('La creation du dossier /home/nagios/downloads a echouer')
		launch(mkdir_downloads_folder , msg, err_msg)
	print ('Fin de la creation et configuration de l\'utilisateur nagios et du groupe nagcmd', file=old_stdout)

	#download nagios core
	if (path.exists('/home/nagios/downloads/nagios-4.4.5.tar.gz') == False):
		url = "https://assets.nagios.com/downloads/nagioscore/releases/nagios-4.4.5.tar.gz"
		dest_path = "/home/nagios/downloads"
		print ('Telechargement de nagios-core')
		wgetfunct(url, dest_path, "nagios-core")
		print ('Fin du telechargement de nagios-core')

	print ('Debut de la configuration de nagios-core', file=old_stdout)
	#decompresse nagios core
	if (path.exists('/home/nagios/downloads/nagios-4.4.5.tar.gz') == True):
		untar_nagios_core = "sudo tar -zxf /home/nagios/downloads/nagios-4.4.5.tar.gz -C /home/nagios/downloads"
		msg = ('Decompression de nagios core avec sucees')
		err_msg = ('La decompression de nagios core a echouer')
		launch(untar_nagios_core , msg, err_msg)

	#configure nagios
	if (path.exists('/home/nagios/downloads/nagios-4.4.5') == True):
		conf_nagios_core = "cd /home/nagios/downloads/nagios-4.4.5 && ./configure --with-httpd-conf=/etc/apache2/sites-enabled --with-command-group=nagcmd"
		msg = ('Configuration de nagios core avec sucees')
		err_msg = ('La configuraion de nagios core a echouer')
		launch(conf_nagios_core , msg, err_msg)

	#make all nagios
	if (path.exists('/home/nagios/downloads/nagios-4.4.5') == True):
		make_all_nagios_core = "cd /home/nagios/downloads/nagios-4.4.5/ && make all"
		msg = ('Make all de nagios core avec sucees')
		err_msg = ('Le make all de nagios core a echouer')
		launch(make_all_nagios_core , msg, err_msg)

	#make all nagios
	if (path.exists('/home/nagios/downloads/nagios-4.4.5') == True):
		make_all_nagios_core = "cd /home/nagios/downloads/nagios-4.4.5/ && make all"
		msg = ('Make all de nagios core avec sucees')
		err_msg = ('Le make all de nagios core a echouer')
		launch(make_all_nagios_core , msg, err_msg)

	#make install nagios
	if (path.exists('/home/nagios/downloads/nagios-4.4.5') == True):
		make_install_nagios_core = "cd /home/nagios/downloads/nagios-4.4.5/ && make install"
		msg = ('Make install de nagios core avec sucees')
		err_msg = ('Le make install de nagios core a echouer')
		launch(make_install_nagios_core , msg, err_msg)

	#make daemon nagios
	if (path.exists('/home/nagios/downloads/nagios-4.4.5') == True):
		make_daemon_nagios_core = "cd /home/nagios/downloads/nagios-4.4.5/ && make install-daemoninit"
		msg = ('Make install-daemoninit de nagios core avec sucees')
		err_msg = ('Le make install-daemoninit de nagios core a echouer')
		launch(make_daemon_nagios_core , msg, err_msg)

	#make command nagios
	if (path.exists('/home/nagios/downloads/nagios-4.4.5') == True):
		make_command_nagios_core = "cd /home/nagios/downloads/nagios-4.4.5/ && make install-commandmode"
		msg = ('Make install-commandmode de nagios core avec sucees')
		err_msg = ('Le make install-commandmode de nagios core a echouer')
		launch(make_command_nagios_core , msg, err_msg)

	#make install-config nagios
	if (path.exists('/home/nagios/downloads/nagios-4.4.5') == True):
		make_instconf_nagios_core = "cd /home/nagios/downloads/nagios-4.4.5/ && make install-config"
		msg = ('Make install-config de nagios core avec sucees')
		err_msg = ('Le make install-config de nagios core a echouer')
		launch(make_instconf_nagios_core , msg, err_msg)

	#make webconf nagios
	if (path.exists('/home/nagios/downloads/nagios-4.4.5') == True):
		make_webconf_nagios_core = "cd /home/nagios/downloads/nagios-4.4.5/ && make install-webconf"
		msg = ('Make install-webconf de nagios core avec sucees')
		err_msg = ('Le make install-webconf de nagios core a echouer')
		launch(make_webconf_nagios_core , msg, err_msg)
	print ('Fin de la configuration de nagios-core', file=old_stdout)
	print ('Debut de la configuration d\'apache', file=old_stdout)
	#configire apache acces
	apache_conf_nagios_core = "htpasswd -cb /usr/local/nagios/etc/htpasswd.users nagiosadmin pass"
	msg = ('Configuration de l\'acces apache avec succes')
	err_msg = ('La Configuration de l\'acces apache a echouer')
	launch(apache_conf_nagios_core , msg, err_msg)

	#chown for nagios right on /usr/local/nagios
	chown_nagios_core = "chown -R nagios:nagcmd /usr/local/nagios"
	msg = ('Dont des droit sur /usr/local/nagios a nagios avec succes')
	err_msg = ('Le dont des droit sur /usr/local/nagios a nagios a echouer')
	launch(chown_nagios_core , msg, err_msg)

	#activate apache module
	apache_module_activ = "a2enmod rewrite && a2enmod cgi"
	msg = ('Activation des module apache avec succes')
	err_msg = ('L\'activation des module apache a echouer')
	launch(apache_module_activ , msg, err_msg)

	#reload apache then start nagios
	systemctl_cmd = "systemctl restart apache2 && systemctl start nagios"
	msg = ('Redemarage d\'apache et demarage de nagios avec succes')
	err_msg = ('Le redemarage d\'apache ou le demarage de nagios a echouer')
	launch(systemctl_cmd , msg, err_msg)
	print ('Fin de la configuration d\'apache', file=old_stdout)

	print ('Fin de l\'installation de nagios-core')
	print ('Fin de l\'installation de nagios-core', file=old_stdout)
	clean_folder()
	close_log('0')

def inst_nagios_plugin():
	#Install required package
	pkg_name_list = ["automake", "libmcrypt-dev", "libssl-dev", "bc", "gawk", "dc", "build-essential", "snmp", "gettext", "default-libmysqlclient-dev"]
	apt_get(pkg_name_list)

	#wget nagios-plugin
	if (path.exists('/home/nagios/downloads/nagios-plugins-2.3.3.tar.gz') == False):
		url = "https://nagios-plugins.org/download/nagios-plugins-2.3.3.tar.gz"
		dest_path = "/home/nagios/downloads"
		print ('Telechargement de nagios-core-plugins')
		wgetfunct(url, dest_path, 'nagios-core-plugin')
		print ('Fin du telechargement de nagios-core-plugins')

	print ('Debut de l\'installation de nagios-core-plugin de nagios-core-plugin', file=old_stdout)
	#untar nagios-plugin
	if (path.exists('/home/nagios/downloads/nagios-plugins-2.3.3.tar.gz') == True):
		untar_nagios_plugin = "sudo tar -zxf /home/nagios/downloads/nagios-plugins-2.3.3.tar.gz -C /home/nagios/downloads"
		msg = ('Decompression de nagios plugin avec sucees')
		err_msg = ('La decompression de nagios plugin a echouer')
		launch(untar_nagios_plugin , msg, err_msg)

	#config nagios-plugin
	if (path.exists('/home/nagios/downloads/nagios-plugins-2.3.3') == True):
		conf_nagios_plugin = "cd /home/nagios/downloads/nagios-plugins-2.3.3 && ./configure --with-nagios-user=nagios --with-nagios-group=nagcmd"
		msg = ('Configuration de nagios plugin avec sucees')
		err_msg = ('La configuraion de nagios plugin a echouer')
		launch(conf_nagios_plugin , msg, err_msg)

	#make nagios plugin
	if (path.exists('/home/nagios/downloads/nagios-plugins-2.3.3') == True):
		make_nagios_plugin = "cd /home/nagios/downloads/nagios-plugins-2.3.3/ && make"
		msg = ('Make de nagios plugin avec sucees')
		err_msg = ('Le make de nagios plugin a echouer')
		launch(make_nagios_plugin , msg, err_msg)

	#make install nagios plugin
	if (path.exists('/home/nagios/downloads/nagios-plugins-2.3.3') == True):
		make_install_nagios_plugin = "cd /home/nagios/downloads/nagios-plugins-2.3.3/ && make install"
		msg = ('Make install de nagios plugin avec sucees')
		err_msg = ('Le make install de nagios plugin a echouer')
		launch(make_install_nagios_plugin , msg, err_msg)

	count_lib_content = "ls /usr/local/nagios/libexec | wc -l"
	msg = "Verification du contenue du dossier /usr/local/nagios/libexec avec succes"
	err_msg = "La verification du contenue du dossier /usr/local/nagios/libexec a echouer"
	test_libexec = launch(count_lib_content, msg, err_msg)
	test_libexec = test_libexec.decode("utf-8")
	if (test_libexec != '0'):
		#reload  nagios
		systemctl_nagios_cmd = "systemctl restart nagios"
		msg = ('Redemarage  de nagios avec succes')
		err_msg = ('Le redemarage de nagios a echouer')
		launch(systemctl_nagios_cmd , msg, err_msg)
	print ('Fin de l\'installation de nagios-core-plugin', file=old_stdout)
	print ('Fin de l\'installation de nagios-core-plugin')
	clean_folder()
	close_log('0')
