#!/usr/bin/env python

import sys

#setting up empty lists
time = []
idMach = []

# input comes from STDIN (standard input)
for line in sys.stdin:
	#every line become a string
    rowString = str(line)
    #split lines by ";"
    rowSplit = rowString.split(";")
    #add elements to list with id
    idMach.append(rowSplit[2])
    #create variable to host time
    timeModify = rowSplit[3]
    #delete the last character of the time
    timeNew = timeModify[:-1]
    #add elements to list with time and converting to int
    time.append(int(timeNew))

#loop to print to STDOUT
for i in range (0, len(time)):
	#create variables to host time and id
    timePrint = time[i]
    idPrint = idMach[i]
    #print keys and values (mapping)
    print('%s\t%i' % (idPrint, timePrint))
