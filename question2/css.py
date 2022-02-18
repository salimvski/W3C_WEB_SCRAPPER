#!/bin/python3
import os
import sys
import argparse
import subprocess
from bs4 import BeautifulSoup

# assign directory
# we get arg from command line when executing ./css.sh [filename]
directory = sys.argv[2]



# la function prend le fichier en argument et le dossier cree en local
# et extrait le code css du fichier et le retourne
def css():
	path = sys.argv[1]

	# Get filename
	file = path.split("/")[-1]


	f = os.path.join(directory, file)
	# checking if it is a file
	if os.path.isfile(f):
		# Open a file: file
		file = open(f,mode='r')
		# read all lines at once
		all_of_it = file.read()
		soup = BeautifulSoup(all_of_it, 'html.parser')
		css = soup.pre.string
		file.close()
		return css
		

if __name__ == "__main__" :
        print(css())
		