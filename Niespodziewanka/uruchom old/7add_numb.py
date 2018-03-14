import os
from random import randint

def addnumb():
	dire = "/Users/pczapla/Documents/marcin/uruchom"
	os.chdir (dire)
	file_list = os.listdir(dire)
	print (file_list)
	for file_name in file_list:
		os.rename (file_name, str(randint(0, 9))+file_name)

addnumb()
