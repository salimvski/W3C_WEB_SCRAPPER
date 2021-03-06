#!/bin/python3
import os
import sys
import argparse
import subprocess
from bs4 import BeautifulSoup

# template in returned by python function
def numberPageNext(number):

	tab = number.split(".")
	nb = tab[4]
	if nb != "172":
		tmp = int(nb) + 1
		return str(tmp)
	else:
		return ""

def numberPagePrev(number):

	tab = number.split(".")
	nb = tab[4]
	if nb == "1":
		return ""
	else:
		tmp = int(nb) - 1
		return str(tmp)



# assign directory
# we get arg from command line when executing ./css.sh [filename]
def readfile():
	f = sys.argv[1]
	file = open(f,mode='r')
	numberNext = numberPageNext(f)
	numberPrev = numberPagePrev(f)
	tmp = f.split(".")
	numberActual = str(tmp[4])

		# read all lines at once
	all_of_it = file.read()
	soup= BeautifulSoup(all_of_it,'html.parser')
	ct = soup.findAll("pre", {"class" : "rules"})
	ct1= ct[0].string
	ct1_bis = ct1.replace("'","/'")
	ct1_bis = ct1.replace("\n", "")
	ct2 = ct[1]
	ct3 = ct[1].string
	file.close()

	html = '''
    <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN">
<html>
<head>
    <title>Template Css</title>
    <!-- CSS only -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script>
    </script>
    <script src="./button.js"></script>
    <style>
        #box1 {
          font-family:"Arial";
          background-color: teal !important;
          text-align: left;
          font-size: 80%;
          padding-top: 5px;
          padding-bottom: 5px;
        }
        a {
            color: white;
        }
        .row{
            position: absolute;
            left: 300px;
            top: 150px;
        }
        .card {
            border-width:1px;
            border-style:solid;
            border-color:black;
            border-spacing: 0px;
            height: 100%;
            width: 300px;
            padding-top: 10px;
            padding-left: 15px;
        }
    </style>
</head>
<body>
    <h1> Testez votre comprehension de CSS</h1>
    <h4>Lisez le css et la structure HTML du test'''+ numberActual + ''', devinez ce que cela devrait produire, puis cliquez sur le bouton solution pour verifier votre reponse</h4>
    <p class="bg-info" id="box1"><a href="./css3.''' + numberPrev + '''.html"> Previous</a> <a href="./css3.''' + numberNext + '''.html">/Next</a></p>
    <div class="container">
        <div class="row">
            <div class="col-4">
                <div class="card">CSS
                    <div class="card-body1">
                        ''' + ct1 + '''
                    </div>
                </div>
            </div>
            <div class="col-4">
                <div class="card">HTML
                    <div class="card-body1">
                        ''' + str(ct2) + '''
                    </div>
                </div>
            </div>
            <div class="col-4">
                <div class="card">
                    <div id="card-body3">
                        <h5 class="card-title"><button onclick="myfunction()"type="button" class="btn btn-danger">Solution</button></h5>
                        <script>
                        function myfunction(){

                        var css = "'''+ str(ct1_bis) +'''";
    head = document.head || document.getElementsByTagName('head')[0],
    style = document.createElement('style');
	head.appendChild(style);
	style.type = 'text/css';
	if (style.styleSheet){
  	// This is required for IE8 and below.
  	style.styleSheet.cssText = css;
} 	else {
  	style.appendChild(document.createTextNode(css));
}
                        }
   
</script>
                        <p class = "card-text3"> ''' + ct3 + ''' </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
'''

	return html
if __name__ == "__main__" :
	print(readfile())