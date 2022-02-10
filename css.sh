#!/bin/bash

count=0
rm -rf cssHTML
mkdir cssHTML
# on traverse les page HTML W3C et on execute le script python pour chaque fichier
# puis on stock le code css dans des pages css en ordre
for FILE in ./tmp/*.html; 
do 

	count=$((count + 1))
	cmd=$(python3 css.py $FILE)
	page="page"$count".css"
	echo $cmd > ./cssHTML/$page
	
done