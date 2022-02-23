#!/bin/bash

count=0
rm -rf cssHTML
mkdir cssHTML

# we go through HTML W3c page and we execute python scrip for each file
# we store css code of the pages within

# how to use ./css.sh [filename]
# use filename of the file created by scrap script
# result be storer in folder cssHTML
for FILE in ./$1/*.html; 
do 
	cmd=$(python3 css.py $FILE $1)
	nameFile=$(basename $FILE)
	page=$nameFile".scss"
	echo $cmd > ./cssHTML/$page
	
done