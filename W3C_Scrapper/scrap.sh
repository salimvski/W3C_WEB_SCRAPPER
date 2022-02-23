#!/bin/bash



# USAGE : ./scrap [file_name_that_youwant]
# The result will be storer in this [file_name_that_youwant]

mkdir $1
wget -r --no-parent --reject "index.html*" https://www.w3.org/Style/CSS/Test/CSS3/Selectors/current/html/full/flat/
mv www.w3.org/Style/CSS/Test/CSS3/Selectors/current/html/full/flat/* $1
rm -rf www.w3.org
i=1
for FILE in ./$1/*.html; 
do 
	mv $FILE "css3."$i".html"
	i=$((i+1))

	
done

cp *.html $1
rm -r *.html