#!/usr/bin/env python

from collections import defaultdict
import sys

#setting up empty default dictionary
diction = defaultdict(int)

# input comes from STDIN (standard input)
for line in sys.stdin:
	#remove whitespaces
	line = line.strip()
	#assign keys and values to variables
	idMach, time = line.split('\t')
	#reducing giving the total value for every key
	diction[idMach] += int(time)

#reordering default dictionary
sortedList = sorted(diction.items())

#loop to print to STDOUT
for i in range(0, len(sortedList)):
	#printing to STDOUT the final result
	print('%s\t%i' % (sortedList[i][0], sortedList[i][1]))