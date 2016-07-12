#!/usr/bin/env python

from collections import defaultdict
import sys


diction = defaultdict(int)

for line in sys.stdin:
	line = line.strip()
	idMach, time = line.split('\t')
	diction[idMach] += int(time)

sortedList = sorted(diction.items())

for i in range(0, len(sortedList)):
	print('%s\t%s' % (sortedList[i][0], sortedList[i][1]))