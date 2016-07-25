#!/usr/bin/env python


import csv
import sys


def map():

	time = []
	total = []
	country = []

	for row in csv.reader(iter(sys.stdin.readline, '')):
		rowString = str(row)
    		rowCleanPartial = rowString[1:]
    		rowCleanTotal = rowCleanPartial[:-1]
    		rowSplit = rowCleanTotal.split(";")
    		try:
    			time.append(rowSplit[0])
    			country.append(rowSplit[2])
    			total.append(rowSplit[6])
		except:
			continue

	timeNew = []
	totalNew = []
	countryNew = []

	for i in range(0, len(time)):
		if '2016' in time[i]:
			timeNew.append(time[i])
			countryNew.append(country[i])
			totalNew.append(total[i])

	for i in range (0, len(countryNew)):
    		totalModify = totalNew[i]
    		totalNumber = int(totalModify[:-1])
    		print('%s\t%f' % (countryNew[i], totalNumber))

if __name__ == '__main__':
    map()