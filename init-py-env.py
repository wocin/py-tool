#!/usr/bin/env python
#By wocin
#Email ---
#init python env
#-------------------I am boring line------------------------------------
import os

def init_first():#init some soft for next
	code=os.system("which pip")
	if code == 0:
		print "pip tools has installed on this system"
	else:
		os.system("yum -y install git python-setuptools python-devel python-docs autoconf gcc")
		os.system("git clone https://github.com/pypa/pip.git")
		os.system("python pip/setup.py build")
		os.system("python pip/setup.py install")
		os.system("mkdir /root/.pip/")
		os.system("touch /root/.pip/pip.conf")
		fpip=open("/root/.pip/pip.conf",'w')
		fpip.write("[global]\nindex-url=http://pypi.v2ex.com/simple\n")
		fpip.close()
		
def main():
	init_first()
	
if __name__ == '__main__':
	main()