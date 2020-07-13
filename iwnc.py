#! /usr/bin/env python3
#Import required python librairies
import os
from os import path
import sys
import subprocess
from subprocess import check_output, CalledProcessError, STDOUT
import argparse
import wget
import ssl
import apt
import apt.progress
from progress.bar import ChargingBar
from termcolor import colored

wordmdp = ''

#Function to close the log file
def close_log(msg_nb):
	log_file.close()
	if (msg_nb == '0'):
		print (colored('Le script c\'est terminer avec succes\nLes log de ce script sont enregistrer dans le fichier iwnc.py.log', 'yellow'))
	if (msg_nb == '1'):
		print (colored('Une erreur est survenu, pour en savoir plus regarder le fichier de log iwnc.py.log', 'red'))

#Function to launch some system cmd with subprocess
def launch(cmd, msg, err_msg):
	try:
		output = check_output(cmd, stderr=STDOUT, shell=True)
		return output
	except CalledProcessError as e:
		print (colored(err_msg, 'red'), file=log_file)
		print (colored(err_msg, 'red'))
		print (colored('Status: FAIL:' + e.output, 'red'), file=log_file)
		clean_folder()
		close_log('1')
		sys.exit(1)
	else:
		print (msg, file=log_file)

#Funciton to delette temporary file/folder
def clean_folder():
	#remove wordpress tar
	if (path.exists(wordpress_tar_path) == True):
		rm_wordpress_tar_cmd = "rm " + wordpress_tar_path
		msg = ('Suppresion de l\'archive wordpress')
		err_msg = ('L\'archive wordpress n\' a pas put etre suprimer')
		launch(rm_wordpress_tar_cmd, msg, err_msg)
	if (path.exists('/tmp/geckodriver-v0.26.0-linux64.tar.gz') == True):
		rm_gecko_cmd = "rm /tmp/geckodriver-v0.26.0-linux64.tar.gz"
		msg = "Suppresion de l\'archive geckodriver"
		err_msg = "La suppresion de l\'archive geckodriver a echouer"
		launch(rm_gecko_cmd, msg, err_msg)

#Class for the apt_get progress bar
class LogInstallProgress(apt.progress.base.InstallProgress):
	def fork(self):
		pid = os.fork()
		if pid == 0:
			os.dup2(logfd, 1)
			os.dup2(logfd, 2)
		return pid

logfd = os.open("inst_apt.log", os.O_RDWR | os.O_APPEND | os.O_CREAT, 0o644)
#function to apt-get some package
def apt_get(pkg_name_list):
	cache = apt.cache.Cache()
	cache.update()
	cache.open()
	print ('Telechargement de ', *pkg_name_list)
	bar = ChargingBar('Telechargement & Installation', max=len(pkg_name_list) + 1)
	bar.next()
	for pkg_name in pkg_name_list:
		pkg = cache[pkg_name]
		if pkg.is_installed:
			print ("\n{pkg_name} est deja installer".format(pkg_name=pkg_name), file=log_file)
			bar.next()
		else:
			pkg.mark_install()

			try:
				cache.commit(install_progress=LogInstallProgress())
				print ("{pkg_name} c\'est installer".format(pkg_name=pkg_name), file=log_file)
				bar.next()
			except (Exception, arg):
				print (colored("l\'installation du packet a echouer [{err}]".format(err=str(arg)), "red"), file=log_file)
	bar.finish()

#Funciton to wget files
def wgetfunct(url, dest_path, name):
	try :
		print ('Debut du telechargement de ', name)
		ssl._create_default_https_context = ssl._create_unverified_context
		wget.download(url, dest_path)
	except:
		print (colored('Une erreur est interveneue dans le telechargement de ' + name, 'red'))
		clean_folder()
		close_log(msg_nb='1')
		sys.exit(1)
	finally:
		print ('\nFin du telechargement de ', name)

def file_search(file, chaine):
	fin = open(file, "rt")
	i = '0'
	for ligne in fin:
		if (chaine in ligne):
			print (chaine, ' est deja definie', file=log_file)
			i = '1'
			fin.close
			break
	return i

#function to add new sonde to nagios-core
def add_cmd_nagios(name1, cmd1, name2, cmd2):
	file = "/usr/local/nagios/etc/objects/commands.cfg"
	tmp = file_search(file, name1)
	if (tmp == '0'):
		fin = open(file, "a+")
		fin.write('\n\ndefine command{\n\tcommand_name ' + name1 + '\n\tcommand_line ' + cmd1 + '\n}')
		fin.close()
	file = "/usr/local/nagios/etc/objects/localhost.cfg"
	tmp = file_search(file, name2)
	if (tmp == '0'):
		fin = open(file, "a+")
		fin.write("\n\ndefine service {\n\tuse local-service\n\thost_name localhost\n\tservice_description " + name2 + "\n\tcheck_command " + cmd2 + "\n}")
		fin.close

#Add geckodriver for selenium lib
def get_geckodriver():
	if (path.exists('/usr/local/bin/geckodriver') == False):
		url = "http://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz"
		dest_path = "/tmp/"
		print ('Telechargement de geckodriver', file=log_file)
		wgetfunct(url, dest_path, 'geckodriver')
		print ('Fin du telechargement de geckodriver', file=log_file)
		if (path.exists('/tmp/geckodriver-v0.26.0-linux64.tar.gz') == True):
			untar_gecko = "tar -C /usr/local/bin -zxf /tmp/geckodriver-v0.26.0-linux64.tar.gz"
			msg = "Decompression de l\'archive geckodriver avec succes"
			err_msg = "La decompresion de l\'archive geckodriver a echouer"
			launch(untar_gecko, msg, err_msg)

		if (path.exists('/usr/local/bin/geckodriver') == True):
			chmod_gecko = "chmod +x /usr/local/bin/geckodriver"
			msg = "Le fichier geckodriver a bien recus les droit d'execution"
			err_msg = "Le fichier geckodriver n\'a pas recus les droit d\'execution"
			launch(chmod_gecko, msg, err_msg)

#Global variables
wordpress_tar_path = '/tmp/wordpress.tar.gz'

#Log file cration
log_file_name = 'iwnc.py.log'
if (path.exists(log_file_name) == False):
	touch_log_file_cmd = "touch " + log_file_name
	msg = 'Creation du fichier de log'
	err_msg = ('Le fichier de log n\'a pas put etre creer')
	launch(touch_log_file_cmd , msg, err_msg)
log_file = open(log_file_name, "w")

#Import secondary files
import wordpress
import nagios
import customPluginNagios

def main():
	parser = argparse.ArgumentParser(description='Permet d\'installer au choix wordpress, nagios-core, les plugins par default de nagios-core, des plugins personaliser de nagios-core, nagios log avec ça sonde pour nagios-core \nPrerequis avant de lancer ce script:\nInstaller python3-pip\nInstaller les librairie python : mysql.connector, wget, progress, selenium')
	parser.add_argument('-w', '--wordpress', action='store_true', default=False, help='Installe apache, wordpress et mysql')
	parser.add_argument('-nc', '--nagioscore', action='store_true', default=False, help='Installe nagios core')
	parser.add_argument('-dp', '--nagiosplugin', action='store_true', default=False, help='Installe nagios core plugins')
	parser.add_argument('-pp', '--nagiospluginpersonalize', action='store_true', default=False, help='Installe nagios core plugins personalisé')
	try:
		args = parser.parse_args()
		print ('Debut du script veuiller patienter')
		w = args.wordpress
		nc = args.nagioscore
		dp = args.nagiosplugin
		pp = args.nagiospluginpersonalize
		if(w == True):
			get_geckodriver()
			wordpress.inst_word()
		if(nc == True):
			nagios.inst_nagios_core()
		elif(dp == True):
			nagios.inst_nagios_plugin()
		if(pp == True):
			customPluginNagios.add_plugin_nagioscore()
		else:
			wordpress.inst_word()
			nagios.inst_nagios_core()
			customPluginNagios.add_plugin_nagioscore()
		clean_folder()
		close_log('0')
	except SystemExit:
		os._exit(0)

if __name__ == '__main__':
	main()
