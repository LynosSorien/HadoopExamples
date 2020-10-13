#!/usr/bin/python
import sys

currentYear = None
maxTemp = None

for entry in sys.stdin:
	year, temp = entry.split("\t", 1)
	temp = float(temp)
	if currentYear == None:
		currentYear = year
		maxTemp = temp
	if currentYear == year and temp > maxTemp:
	        maxTemp = temp
	elif currentYear != year:
		print("%s\t%s" % (currentYear, maxTemp))
		currentYear = year
		maxTemp = temp

print("%s\t%s" % (currentYear, maxTemp))
