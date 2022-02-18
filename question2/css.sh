#!/bin/bash

count=0
rm -rf cssHTML
mkdir cssHTML
# on traverse les page HTML W3C et on execute le script python pour chaque fichier
# puis on stock le code css dans des pages css en ordre
# how to use ./css.sh [filename]
# meme filename que dans scrap utilise
for FILE in ./$1/*.html; 
do 
	cmd=$(python3 css.py $FILE $1)
	nameFile=$(basename $FILE)
	page=$nameFile".scss"
	echo $cmd > ./cssHTML/$page
	
done