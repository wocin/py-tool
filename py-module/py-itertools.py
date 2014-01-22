#!/usr/bin/env python
#By wocin
#Email ---
#python itertools module
'''
from itertools import chain
test=chain.from_iterable('ABCDEFG')
test.next()

same to

def iter(iter):
	for x in iter:
		for y in x:
			yield y
test=iter('ABCDEFG')
test.next()
'''