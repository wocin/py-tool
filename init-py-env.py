#!/usr/bin/env python
#By wocin
#Email ---
#init python env
#-------------------I am boring line------------------------------------
import os
import subprocess

def init_first():#init some soft for next
	os.system("yum -y install git python-setuptools")
	os.system("git clone")
def init_pip():#init pip
	os.system("cd pip")
	os.system("python setup.py install")
def init_virt_fab():#init virtualenv and fabric

def init_salt_ansbile():#init saltstrack and ansible

def clean():#Delete the installation package

def main():
	init_first()
	init_pip()
	init_virt_fab()
	init_salt_ansible()
if __name__ == '__main__':
	main()
