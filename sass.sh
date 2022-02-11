#!/bin/bash

rm -rf validyCSS
mkdir validyCSS
for FILE in ./$1/*.scss; 
do 
	# execute sass command to compile scss file
	# redirect errors also
	result=$(sass $FILE 2>&1)
	nameFile=$(basename $FILE)
	page=$nameFile".log"
	error="Error"
	# if result contains Error message we create page and put error within
	if [[ "$result" == *"$error"* ]]; then
		echo "error"
		echo $result > ./validyCSS/$page
	fi
	
done