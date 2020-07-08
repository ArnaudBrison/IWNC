from main import apt_get, wgetfunct, launch, clean_folder, close_log, add_cmd_nagios, file_search
from os import path

def add_plugin_nagioscore():

	if (path.exists('/usr/local/nagios') == True):
		#plugin check_ddos
		if(path.exists('/usr/local/nagios/libexec/check_ddos.py') == False):
			pkg_name_list = ["net-tools"]
			apt_get(pkg_name_list)
			url = 'https://exchange.nagios.org/components/com_mtree/attachment.php?link_id=7074&cf_id=24'
			dest_path = '/usr/local/nagios/libexec/'
			wgetfunct(url, dest_path, 'check_ddos')
		if(path.exists('/usr/local/nagios/libexec/check_ddos.py') == True):
			print ('Configuration du plugin check_ddos', file=old_stdout)
			file = '/usr/local/nagios/libexec/check_ddos.py'
			chaine = '#! /usr/bin/env python3'
			result = file_search(file, chaine)
			if (result == '0'):
				fin = open("/usr/local/nagios/libexec/check_ddos.py", "rt")
				data = fin.read()
				data = data.replace('#! /usr/bin/env python', '#! /usr/bin/env python3')
				fin.close()
				fin = open("/usr/local/nagios/libexec/check_ddos.py", "wt")
				fin.write(data)
				fin.close()

			chmod_check_ddos = "chmod +x /usr/local/nagios/libexec/check_ddos.py"
			msg = "Le fichier check_ddos.py a bien recus les droit d'execution"
			err_msg = "Le fichier check_ddos.py n\'a pas recus les droit d\'execution"
			launch(chmod_check_ddos, msg, err_msg)

			name1 = "check_ddos"
			cmd1 = "$USER1$/check_ddos.py -c $ARG1$ -w $ARG2$"
			name2 = name1
			cmd2 = "check_ddos!300!200"
			add_cmd_nagios(name1, cmd1, name2, cmd2)

		#plugin check_service.sh
		if(path.exists('/usr/local/nagios/libexec/check_service.sh') == False):
			url = 'https://raw.githubusercontent.com/jonschipp/nagios-plugins/master/check_service.sh'
			dest_path = '/usr/local/nagios/libexec/'
			wgetfunct(url, dest_path, 'check_service')

		if(path.exists('/usr/local/nagios/libexec/check_service.sh') == True):
			print ('Configuration du plugin check_service', file=old_stdout)
			chmod_check_service = "chmod +x /usr/local/nagios/libexec/check_service.sh"
			msg = "Le fichier check_service.sh a bien recus les droit d'execution"
			err_msg = "Le fichier check_service.sh n\'a pas recus les droit d\'execution"
			launch(chmod_check_service, msg, err_msg)

			name1 = "check_service"
			cmd1 = "$USER1$/check_service.sh -o $ARG1$ -s $ARG2$"
			name2 = "check_service_nagios-core"
			cmd2 = "check_service!linux!nagios"
			add_cmd_nagios(name1, cmd1, name2, cmd2)

		#plugin check_website_speed
		if(path.exists('/usr/local/nagios/libexec/check_website_speed.php') == False):
			url = 'https://exchange.nagios.org/components/com_mtree/attachment.php?link_id=1898&cf_id=24'
			dest_path = '/usr/local/nagios/libexec/'
			wgetfunct(url, dest_path, 'check_webiste_speed')

		if(path.exists('/usr/local/nagios/libexec/check_website_speed.php') == True):
			print ('Configuration du plugin check_website_speed', file=old_stdout)
			chmod_check_website_speed = "chmod +x /usr/local/nagios/libexec/check_website_speed.php"
			msg = "Le fichier check_website_speed.php a bien recus les droit d'execution"
			err_msg = "Le fichier check_website_speed.php n\'a pas recus les droit d\'execution"
			launch(chmod_check_website_speed, msg, err_msg)

			file = '/usr/local/nagios/libexec/check_website_speed.php'
			chaine = '<?php'
			result = file_search(file, chaine)

			if (result == '0'):
				fin = open("/usr/local/nagios/libexec/check_website_speed.php", "rt")
				data = fin.read()
				data = data.replace('<?', '<?php')
				fin.close()
				fin = open("/usr/local/nagios/libexec/check_website_speed.php", "wt")
				fin.write(data)
				fin.close()

			name1 = "check_website_speed"
			cmd1 = "php $USER1$/check_website_speed.php $ARG1$ $ARG2$ $ARG3$"
			name2 = name1
			cmd2 = "check_website_speed!http://127.0.0.1/wordpress/!2!4"
			add_cmd_nagios(name1, cmd1, name2, cmd2)

		#plugin check_wp_version
		if(path.exists('/usr/local/nagios/libexec/check_wp_version') == False):
			url = 'https://exchange.nagios.org/components/com_mtree/attachment.php?link_id=2371&cf_id=24'
			dest_path = '/usr/local/nagios/libexec/'
			wgetfunct(url, dest_path, 'check_wp_version')

		if(path.exists('/usr/local/nagios/libexec/check_wp_version') == True):
			print ('Configuration du plugin check_wp-version', file=old_stdout)
			chmod_check_wp_version = "chmod +x /usr/local/nagios/libexec/check_wp_version"
			msg = "Le fichier check_wp_version a bien recus les droit d'execution"
			err_msg = "Le fichier check_wp_version n\'a pas recus les droit d\'execution"
			launch(chmod_check_wp_version, msg, err_msg)

			name1 = "check_wp_version"
			cmd1 = "$USER1$/check_wp_version $ARG1$"
			name2 = name1
			cmd2 = "check_wp_version!/var/www/html/wordpress/"
			add_cmd_nagios(name1, cmd1, name2, cmd2)

		#plugin check_url_status
		if(path.exists('/usr/local/nagios/libexec/check_url_status*') == False):
			pkg_name_list = ["libwww-perl"]
			apt_get(pkg_name_list)
			url = 'https://exchange.nagios.org/components/com_mtree/attachment.php?link_id=1396&cf_id=24'
			dest_path = '/usr/local/nagios/libexec/'
			wgetfunct(url, dest_path, 'check_url_status')

		if(path.exists('/usr/local/nagios/libexec/check_url_status*') == True):
			print ('Configuration du plugin check_url_status', file=old_stdout)
			mv_to_check_url = "mv /usr/local/nagios/libexec/check_url_status* /usr/local/nagios/libexec/check_url_status"
			msg = "Le fichier check_url_status_*(num vers) a ete transformer en nom standart check_url_staus"
			err_msg = ("Le fichier check_url_status_*(num ver) na pas ete transformer en nom standart")
			launch(mv_to_check_url, msg, err_msg)

			chmod_check_website_status = "chmod +x /usr/local/nagios/libexec/check_url_status"
			msg = "Le fichier check_url_status a bien recus les droit d'execution"
			err_msg = "Le fichier check_url_status n\'a pas recus les droit d\'execution"
			launch(chmod_check_website_status, msg, err_msg)

			name1 = "check_url_status"
			cmd1 = "$USER1$/check_url_status -U $ARG1$"
			name2 = name1
			cmd2 = "check_url_status!http://127.0.0.1/wordpress/"
			add_cmd_nagios(name1, cmd1, name2, cmd2)

		#plugin check_mysql
		if(path.exists('/usr/local/nagios/libexec/check_mysql') == True):
			print ('Configuration du plugin check_mysql', file=old_stdout)
			chmod_check_website_status = "chmod +x /usr/local/nagios/libexec/check_mysql"
			msg = "Le fichier check_mysql a bien recus les droit d'execution"
			err_msg = "Le fichier check_mysql n\'a pas recus les droit d\'execution"
			launch(chmod_check_website_status, msg, err_msg)

			name1 = "check_mysql"
			cmd1 = "$USER1$/check_mysql -H $HOSTADDRESS$ -u $ARG1$ -p $ARG2$"
			name2 = name1
			cmd2 = "check_mysql!wordpress!Yters3/jfg"
			add_cmd_nagios(name1, cmd1, name2, cmd2)

		#reload  nagios
		systemctl_nagios_cmd = "systemctl restart nagios"
		msg = ('Redemarage  de nagios avec succes')
		err_msg = ('Le redemarage de nagios a echouer')
		launch(systemctl_nagios_cmd , msg, err_msg)
		print ('Fin de l\'installation des plugin nagios-core personnaliser', file=old_stdout)
		print ('Fin de l\'installation des plugin nagios-core personnaliser')
		clean_folder()
		close_log('0')
