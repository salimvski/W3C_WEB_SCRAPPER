
# program qui prend le fichier genere par scrap en argument et genere beautified 
# utilisation : ./transh [filename]



mkdir $2
for FILE in ./$1/*.html; 
do 
	nameFile=$(basename $FILE)
	python3 injector.py $FILE > ./$2/$nameFile
	
done