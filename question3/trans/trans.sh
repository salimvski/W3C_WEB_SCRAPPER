

rm -rf beautified
mkdir beautified
for FILE in ./$1/*.html; 
do 
	nameFile=$(basename $FILE)
	python3 injector.py $FILE > ./beautified/$nameFile
	
done