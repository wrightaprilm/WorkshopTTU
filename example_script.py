#!/usr/bin/env python

import sys

last_name = sys.argv[1]
key = sys.argv[2]

def filter_name(last_name, key):
	positives = []
	negatives = []
	for letter in last_name:
		if letter == key:
			positives.append(letter)
		else: 
			negatives.append(letter)
	print negatives, positives
	return([positives, negatives])

filter_name(last_name, key)


