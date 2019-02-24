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
for i in range(1,29):
	print ("Reading file: ", i)
	filename = '/home/aman/Desktop/AI_Project/Data Set/'+str(i)+'.json'
	with open(filename) as data_file:    
		data = json.load(data_file)

	for reviews in data["reviews"]:
		lines = reviews["review"].splitlines()
		ratWords = lines[0].split()
		rating = ratWords[0]
		rating = float(rating)
		comment = ""
		if rating >= 3.0:
			sentiment = 1
		else:
			sentiment = 0
		j = 4
		if lines[3] == "Verified Purchase":
			comment = lines[4]
		elif lines[3].startswith("Hardware Platform:"):
			if lines[4] == "|":
				if lines[5] == "Verified Purchase":
					comment = lines[6]
					j = 7
				else:
					comment = lines[5]
					j = 6
			elif lines[4] == "Verified Purchase":
				comment = lines[5]
				j = 6
			else:
				comment = lines[4]
				j = 5
		else:
			comment = lines[3]
			j = 4
		while "Comment" not in lines[j] and "Comments" not in lines[j]:
			comment += lines[j]
			j += 1
		f = ""
		if(sentiment == 1):
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
		
			if posrevthou == 0:
				f = "/home/aman/Desktop/AI_Project/ParsedDataSet/pos/cv"+str(posrevhun)+""+str(posrevten)+""+str(posrevone)+".txt"
			else:
				f = "/home/aman/Desktop/AI_Project/ParsedDataSet/pos/cv"+str(posrevthou)+""+str(posrevhun)+""+str(posrevten)+""+str(posrevone)+".txt"
		else:
			negrevone = negrevone+1
			if negrevone == 10:
				negrevone = 0
				negrevten = negrevten+1
			if negrevten == 10:
				negrevten = 0
				negrevhun = negrevhun+1
			if negrevthou == 10:
				negrevhun = 0
				negrevthou = negrevthou+1
			if negrevthou == 0:
				f = "/home/aman/Desktop/AI_Project/ParsedDataSet/neg/cv"+str(negrevhun)+""+str(negrevten)+""+str(negrevone)+".txt"
			else:
				f = "/home/aman/Desktop/AI_Project/ParsedDataSet/neg/cv"+str(negrevthou)+""+str(negrevhun)+""+str(negrevten)+""+str(negrevone)+".txt"
		outfile = open(f,'w+')
		outfile.write(comment+"\n")
		outfile.close()