import sys 
import subprocess

from MongoManager import MongoManager
from CertManager import CertManager

mm = MongoManager()
cm = CertManager()

def add_server(user, alias, ssh_string): 
	cert_name = user + '_' + alias
	cm.add_cert(cert_name)
	mm.add_server(user, ssh_string, alias, cert_name)
	cm.upload_cert(cert_name, ssh_string)

	cert_path = cm.get_cert_path(cert_name) 
	

def remove_server 
if __name__ == '__main__':
	action, target = sys.argv[1:3]
	fedssh_args = sys.argv[3:]

	if action == 'add':
		if target == 'server':
			add_server(*fedssh_args)

	if action == 'remove':
		if target == 'server':