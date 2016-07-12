#!/usr/bin/env python

import sys


time = []
idMach = []

for line in sys.stdin:
    rowString = str(line)
    rowSplit = rowString.split(";")
    idMach.append(rowSplit[2])
    timeModify = rowSplit[3]
    timeNew = timeModify[:-1]
    time.append(int(timeNew))

for i in range (0, len(time)):
    timePrint = time[i]
    idPrint = idMach[i]
    print('%s\t%s' % (idPrint, timePrint))
