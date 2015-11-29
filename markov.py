from collections import OrderedDict

def Markov(fileName): 
	# open txt file 
	with open(fileName) as fileName: 
		text = fileName.read() 

	# crawl txt file and create array of words
	textArray = text.split(' ') 


	frequencyDict = {}
	for word in textArray:
		frequencyDict[word] = []


	# go through text file and add the word after it 
	for i in range(0, len(textArray - 1)):
		frequencyDict[textArray[i]].append(textArray[i+1])

	length = random.randint(10, 15) 

	seed = random.randint(0, len(frequencyDict) - 1)

	sentence_data = [frequencyDict[seed]]
	current_word = frequencyDIct[seed] 

	while len(sentence_data) < length: 
		



		 
		


