#!/bin/python3
import os
import sys
import argparse
import subprocess
from bs4 import BeautifulSoup


# assign directory
# we get arg from command line when executing ./css.sh [filename]
def readfile():
	f = sys.argv[1]

	file = open(f,mode='r')
		# read all lines at once
	all_of_it = file.read()
	soup= BeautifulSoup(all_of_it,'html.parser')
	ct = soup.findAll("pre", {"class" : "rules"})
	ct1= ct[0].string
	ct2 = ct[1]
	ct3 = ct[1].string
	file.close()

	html = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN">
<html>

<head>
    <title>Template Css</title>
    <!-- CSS only -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>

<body>
    <h1> Testez votre comprehension de CSS</h1>
    <p>Lisez le css et la structure HTML du test2, devinez ce que cela devrait produire, puis cliquez sur le bouton solution pour verifier votre reponse</p>
    <p class="bg-info"><a href=""> Previous</a> <a href="">/Next</a></p>
    <div class="container">
        <div class="row">
            <div class="col-4">
                <div class="card">CSS
                    <div class="card-body">
                        <p class="card-text"> ''' + ct1 +'''</p>
                    </div>
                </div>
            </div>
            <div class="col-4">
                <div class="card">HTML
                    <div class="card-body">
                        <p class="card-text"> ''' + str(ct2) + '''<p>
                    </div>
                </div>
            </div>
            <div class="col-4">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title"><button type="button" class="btn btn-danger">Danger</button></h5>
                        <p class="card-text"> ''' + ct3 + '''</p>
                        <a href="#" class="btn btn-primary">Go somewhere</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>

</html>'''

	return html
if __name__ == "__main__" :
	print(readfile())