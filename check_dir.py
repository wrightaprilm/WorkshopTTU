#!/usr/bin/env python
import os

def search_dir():
	'''short function to check if there is a processed directory'''
	if 'processed' in os.listdir('.'):
		print 'Processed directory exists'
	else:
		os.mkdir('processed')
		print 'Processed directory created' 

	return(0)

if __name__ == '__main__':
	import os
	search_dir()

