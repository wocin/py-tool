#!/usr/bin/env python
#coding=utf-8
import urllib2 
import simplejson 
import sys
def get_location():
	ipadd = open(sys.argv[1],'r').readlines()
	for ip in ipadd:
		url = 'http://ip.taobao.com/service/getIpInfo.php?ip=%s' % ip
		context = urllib2.urlopen(url).read()  
		status = simplejson.loads(context) 
		print '%s \t\t--- %s %s %s' %(ip,status['data']['region'],status['data']['city'],status['data']['isp'])

if __name__ == '__main__':
	get_location()