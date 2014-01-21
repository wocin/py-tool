#!/usr/bin/env python
#By wocin
#Email ---
#choice init python module
#-------------------I am boring line------------------------------------
import sys,subprocess

def init(mod):
	code=subprocess.call('python -c "import %s"' %mod,shell=True)
	if code == 0:
		print '%s module has installed' %mod
	else:
		subprocess.call('pip install %s' %mod,shell=True)

if __name__ == '__main__':
	mod=sys.argv[1]
	init(mod)