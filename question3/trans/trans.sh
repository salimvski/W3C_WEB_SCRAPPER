
# program qui prend le fichier genere par scrap en argument et genere beautified 
# utilisation : ./transh [filename]

rm -rf beautified
mkdir beautified
for FILE in ./$1/*.html; 
do 
	nameFile=$(basename $FILE)
	python3 injector.py $FILE > ./beautified/$nameFile
	
done