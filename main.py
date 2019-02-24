import json
import os
from pprint import pprint

resp = 1
while resp == 1 or resp == 2 or resp == 3:
	print ("\nWould you like to: \n1. Train the Sentiment Analyzer\n2. Check a particular review\n3. Test the Sentiment Analyzer\n4. Exit")
	resp = input();
	resp = int(resp);
	if resp == 1:
		i=4;
		for i in range(4,29):
			print ("Reading file: ", i)
			filename = '/home/aman/Desktop/AI_Project/Data Set/'+str(i)+'.json'
			with open(filename) as data_file:    
				data = json.load(data_file)

			with open('/home/aman/Desktop/AI_Project/Sentiment Dictionary/incwords.json') as data_file2:    
				incwdata = json.load(data_file2)
			
			with open('/home/aman/Desktop/AI_Project/Sentiment Dictionary/decwords.json') as data_file3:    
				decwdata = json.load(data_file3)
		
			with open('/home/aman/Desktop/AI_Project/Sentiment Dictionary/invwords.json') as data_file4:    
				invwdata = json.load(data_file4)

			for reviews in data["reviews"]:
				lines = reviews["review"].splitlines()
				ratWords = lines[0].split()
				rating = ratWords[0]
				rating = float(rating)
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
				comment = list(comment);
				i = 0;
				for i in range(len(comment)):
					if comment[i] == ',' or comment[i] == '.':
						comment[i] = ' ';
				comment = "".join(comment)
				words = comment.split();
				for word in words:
					word = word.lower()
					chk = 0
					for nword in incwdata["words"]:
						if word == nword:
							chk = 1
							break
					if chk == 1:
						continue
					chk = 0
					for nword in decwdata["words"]:
						if word == nword:
							chk = 1
							break
					if chk == 1:
						continue
					chk = 0
					for nword in invwdata["words"]:
						if word == nword:
							chk = 1
							break
					if chk == 1:
						continue
					if sentiment == 1:	
						with open('/home/aman/Desktop/AI_Project/Sentiment Dictionary/poswordfreq.json', 'r') as f1:
							pdata = json.load(f1)
							pdata["no_of_words"] = str(int(pdata["no_of_words"])+1)
							try:
								pdata[word] = str(int(pdata[word])+1)
							except Exception:
								pdata[word] = 1
						os.remove('/home/aman/Desktop/AI_Project/Sentiment Dictionary/poswordfreq.json')
						with open('/home/aman/Desktop/AI_Project/Sentiment Dictionary/poswordfreq.json', 'w') as f1:
							json.dump(pdata, f1, indent=4)			
					else:
						with open('/home/aman/Desktop/AI_Project/Sentiment Dictionary/negwordfreq.json', 'r') as f1:
							pdata = json.load(f1)
							pdata["no_of_words"] = str(int(pdata["no_of_words"])+1)
							try:
								pdata[word] = str(int(pdata[word])+1)
							except Exception:
								pdata[word] = 1
						os.remove('/home/aman/Desktop/AI_Project/Sentiment Dictionary/negwordfreq.json')
						with open('/home/aman/Desktop/AI_Project/Sentiment Dictionary/negwordfreq.json', 'w') as f1:
							json.dump(pdata, f1, indent=4)
	elif resp == 2:
		print ("Enter the comment: ")
		cmt = input()
		cmt = list(cmt);
		i = 0;
		for i in range(len(cmt)):
			if cmt[i] == ',' or cmt[i] == '.':
				cmt[i] = ' ';
		cmt = "".join(cmt)
		cmtwords = cmt.split();
		with open('/home/aman/Desktop/AI_Project/Sentiment Dictionary/incwords.json') as data_file2:    
			incwdata = json.load(data_file2)
			
		with open('/home/aman/Desktop/AI_Project/Sentiment Dictionary/decwords.json') as data_file3:    
			decwdata = json.load(data_file3)
		
		with open('/home/aman/Desktop/AI_Project/Sentiment Dictionary/invwords.json') as data_file4:    
			invwdata = json.load(data_file4)
		
		with open('/home/aman/Desktop/AI_Project/Sentiment Dictionary/poswordfreq.json') as pf:    
			poswdata = json.load(pf)
			
		with open('/home/aman/Desktop/AI_Project/Sentiment Dictionary/negwordfreq.json') as pf:    
			negwdata = json.load(pf)
			
		chk = 0
		posprodprob = 1
		negprodprob = 1
		for word in cmtwords:
			word = word.lower()
			if chk == 0 or chk == 4:
				for nword in incwdata["words"]:
					if word == nword:
						chk = 1
						break
				if chk != 0:
					continue
				for nword in decwdata["words"]:
					if word == nword:
						chk = 2
						break
				if chk != 0:
					continue
				for nword in invwdata["words"]:
					if word == nword:
						chk = 3
						break
				if chk != 0:
					continue
				cnt = 0
				try:
					cnt = int(poswdata[word])
				except Exception:
					cnt = int(poswdata["no_of_words"])
				posprodprob = posprodprob * (cnt/int(poswdata["no_of_words"]))
			
				try:
					cnt = int(negwdata[word])
				except Exception:
					cnt = int(negwdata["no_of_words"])
				negprodprob = negprodprob * (cnt/int(negwdata["no_of_words"]))
			elif chk == 1:
				chk = 0
				for nword in incwdata["words"]:
					if word == nword:
						chk = 1
						break
				if chk != 0:
					continue
				for nword in decwdata["words"]:
					if word == nword:
						chk = 2
						break
				if chk != 0:
					continue
				for nword in invwdata["words"]:
					if word == nword:
						chk = 3
						break
				if chk != 0:
					continue
				cnt = 0
				try:
					cnt = int(poswdata[word])
				except Exception:
					cnt = int(poswdata["no_of_words"])*0.5
				posprodprob = posprodprob * ((cnt*2)/int(poswdata["no_of_words"]))
			
				try:
					cnt = int(negwdata[word])
				except Exception:
					cnt = int(negwdata["no_of_words"])*0.5
				negprodprob = negprodprob * ((cnt*2)/int(negwdata["no_of_words"]))
			elif chk == 2:
				chk = 0
				for nword in incwdata["words"]:
					if word == nword:
						chk = 1
						break
				if chk != 0:
					continue
				for nword in decwdata["words"]:
					if word == nword:
						chk = 2
						break
				if chk != 0:
					continue
				for nword in invwdata["words"]:
					if word == nword:
						chk = 3
						break
				if chk != 0:
					continue
				cnt = 0
				try:
					cnt = int(poswdata[word])
				except Exception:
					cnt = int(poswdata["no_of_words"])*2
				posprodprob = posprodprob * ((cnt*0.5)/int(poswdata["no_of_words"]))
			
				try:
					cnt = int(negwdata[word])
				except Exception:
					cnt = int(negwdata["no_of_words"])*2
				negprodprob = negprodprob * ((cnt*0.5)/int(negwdata["no_of_words"]))
			elif chk == 3:
				chk = 0
				for nword in incwdata["words"]:
					if word == nword:
						chk = 2
						break
				if chk != 0:
					continue
				for nword in decwdata["words"]:
					if word == nword:
						chk = 1
						break
				if chk != 0:
					continue
				for nword in invwdata["words"]:
					if word == nword:
						chk = 4
						break
				if chk != 0:
					continue
				cnt = 0
				try:
					cnt = int(poswdata[word])
				except Exception:
					cnt = int(poswdata["no_of_words"])
				negprodprob = negprodprob * (cnt/int(poswdata["no_of_words"]))
			
				try:
					cnt = int(negwdata[word])
				except Exception:
					cnt = int(negwdata["no_of_words"])
				posprodprob = posprodprob * (cnt/int(negwdata["no_of_words"]))
			
		posw = int(poswdata["no_of_words"])
		negw = int(negwdata["no_of_words"])
		posprob = posprodprob * (posw/(posw+negw))
		negprob = negprodprob * (negw/(posw+negw))
		print ("\n",posprob, " : ", negprob,"\n")
		if posprob > negprob:
			print ("The comment is Positive!")
		else:
			print ("The comment is Negative!")
	elif resp == 3:
		ptp = 0
		pfp = 0
		pfn = 0
		ntp = 0
		nfp = 0
		nfn = 0
		for i in range(1,4):
			print ("Reading file: ", i)
			filename = '/home/aman/Desktop/AI_Project/Data Set/'+str(i)+'.json'
			with open(filename) as data_file:    
				data = json.load(data_file)
			for reviews in data["reviews"]:
				lines = reviews["review"].splitlines()
				ratWords = lines[0].split()
				rating = ratWords[0]
				rating = float(rating)
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
				comment = list(comment);
				i = 0;
				for i in range(len(comment)):
					if comment[i] == ',' or comment[i] == '.':
						comment[i] = ' ';
				cmt = "".join(comment)
				cmtwords = cmt.split();
				with open('/home/aman/Desktop/AI_Project/Sentiment Dictionary/incwords.json') as data_file2:    
					incwdata = json.load(data_file2)
			
				with open('/home/aman/Desktop/AI_Project/Sentiment Dictionary/decwords.json') as data_file3:    
					decwdata = json.load(data_file3)
		
				with open('/home/aman/Desktop/AI_Project/Sentiment Dictionary/invwords.json') as data_file4:    
					invwdata = json.load(data_file4)
		
				with open('/home/aman/Desktop/AI_Project/Sentiment Dictionary/poswordfreq.json') as pf:    
					poswdata = json.load(pf)
			
				with open('/home/aman/Desktop/AI_Project/Sentiment Dictionary/negwordfreq.json') as pf:    
					negwdata = json.load(pf)
			
				chk = 0
				posprodprob = 1
				negprodprob = 1
				for word in cmtwords:
					word = word.lower()
					if chk == 0 or chk == 4:
						for nword in incwdata["words"]:
							if word == nword:
								chk = 1
								break
						if chk != 0:
							continue
						for nword in decwdata["words"]:
							if word == nword:
								chk = 2
								break
						if chk != 0:
							continue
						for nword in invwdata["words"]:
							if word == nword:
								chk = 3
								break
						if chk != 0:
							continue
						cnt = 0
						try:
							cnt = int(poswdata[word])
						except Exception:
							cnt = int(poswdata["no_of_words"])
						posprodprob = posprodprob * (cnt/int(poswdata["no_of_words"]))
			
						try:
							cnt = int(negwdata[word])
						except Exception:
							cnt = int(negwdata["no_of_words"])
						negprodprob = negprodprob * (cnt/int(negwdata["no_of_words"]))
					elif chk == 1:
						chk = 0
						for nword in incwdata["words"]:
							if word == nword:
								chk = 1
								break
						if chk != 0:
							continue
						for nword in decwdata["words"]:
							if word == nword:
								chk = 2
								break
						if chk != 0:
							continue
						for nword in invwdata["words"]:
							if word == nword:
								chk = 3
								break
						if chk != 0:
							continue
						cnt = 0
						try:
							cnt = int(poswdata[word])
						except Exception:
							cnt = int(poswdata["no_of_words"])*0.5
						posprodprob = posprodprob * ((cnt*2)/int(poswdata["no_of_words"]))
			
						try:
							cnt = int(negwdata[word])
						except Exception:
							cnt = int(negwdata["no_of_words"])*0.5
						negprodprob = negprodprob * ((cnt*2)/int(negwdata["no_of_words"]))
					elif chk == 2:
						chk = 0
						for nword in incwdata["words"]:
							if word == nword:
								chk = 1
								break
						if chk != 0:
							continue
						for nword in decwdata["words"]:
							if word == nword:
								chk = 2
								break
						if chk != 0:
							continue
						for nword in invwdata["words"]:
							if word == nword:
								chk = 3
								break
						if chk != 0:
							continue
						cnt = 0
						try:
							cnt = int(poswdata[word])
						except Exception:
							cnt = int(poswdata["no_of_words"])*2
						posprodprob = posprodprob * ((cnt*0.5)/int(poswdata["no_of_words"]))
			
						try:
							cnt = int(negwdata[word])
						except Exception:
							cnt = int(negwdata["no_of_words"])*2
						negprodprob = negprodprob * ((cnt*0.5)/int(negwdata["no_of_words"]))
					elif chk == 3:
						chk = 0
						for nword in incwdata["words"]:
							if word == nword:
								chk = 2
								break
						if chk != 0:
							continue
						for nword in decwdata["words"]:
							if word == nword:
								chk = 1
								break
						if chk != 0:
							continue
						for nword in invwdata["words"]:
							if word == nword:
								chk = 4
								break
						if chk != 0:
							continue
						cnt = 0
						try:
							cnt = int(poswdata[word])
						except Exception:
							cnt = int(poswdata["no_of_words"])
						negprodprob = negprodprob * (cnt/int(poswdata["no_of_words"]))
			
						try:
							cnt = int(negwdata[word])
						except Exception:
							cnt = int(negwdata["no_of_words"])
						posprodprob = posprodprob * (cnt/int(negwdata["no_of_words"]))
			
				posw = int(poswdata["no_of_words"])
				negw = int(negwdata["no_of_words"])
				posprob = posprodprob * (posw/(posw+negw))
				negprob = negprodprob * (negw/(posw+negw))
				if posprob > negprob:
					if sentiment == 1:
						ptp += 1
					else:
						pfp += 1
						nfn += 1
				else:
					if sentiment == 0:
						ntp += 1
					else:
						nfp += 1
						pfn += 1
		print ("Precision: \npos: "+str(ptp/(ptp+pfp))+"\nneg: "+str(ntp/(ntp+nfp)))
		print ("Recall: \npos: "+str(ptp/(ptp+pfn))+"\nneg: "+str(ntp/(ntp+nfn)))