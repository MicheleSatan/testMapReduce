#!/usr/bin/env python

from collections import defaultdict
import sys


def reduce():
	
	diction = defaultdict(float)
	
	for line in sys.stdin:
		line = line.strip()
		country, total = line.split('\t')
		diction[country] += float(total)
		
	for i in diction:
		print('%s\t%i' % (i, diction[i]))

if __name__ == '__main__':
    reduce()