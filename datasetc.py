import json
import os
from pprint import pprint

posrevone = 0
posrevten = 0
posrevhun = 0
posrevthou = 0
negrevone = 0
negrevten = 0
negrevhun = 0
negrevthou = 0
curcnt = 998
for i in range(1,2):
	print ("Reading file: ", i)
	posrevone = posrevone + 1
	if posrevone == 10:
		posrevone = 0
		posrevten = posrevten+1
	if posrevten == 10:
		posrevten = 0
		posrevhun = posrevhun+1
	if posrevthou == 10:
		posrevhun = 0
		posrevthou = posrevthou+1
	
	infile = open("/home/aman/Desktop/AI_Project/ParsedDataSet/neg/cv"+str(posrevhun)+""+str(posrevten)+""+str(posrevone)+".txt",'r')
	data = infile.read()
	fn = curcnt+i
	outfile = open("/home/aman/Desktop/AI_Project/ParsedDataSet/neg/cv"+str(fn)+".txt",'w+')
	outfile.write(data)
	
	infile.close()
	outfile.close()