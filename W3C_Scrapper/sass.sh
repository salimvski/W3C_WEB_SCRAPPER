#!/bin/bash

rm -rf validyCSS
mkdir validyCSS
for FILE in ./$1/*.scss; 
do 
	
	# we execute sass command for each file 
	# we redirect errors in file
	result=$(sass $FILE 2>&1)
	nameFile=$(basename $FILE)
	page=$nameFile".log"
	error="Error"
	# if result contains Error message we create page and put error within
	if [[ "$result" == *"$error"* ]]; then
		echo $result > ./validyCSS/$page
	fi
	
done