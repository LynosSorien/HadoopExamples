#!/usr/bin/python
import sys

for line in sys.stdin:
  line = line.strip()
  year, month, temp = line.split("\t", 2)
  print("%s\t%s" % (year, temp))
