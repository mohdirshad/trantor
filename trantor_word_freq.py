from trantor_clean_words import cleanwords

def wordfreq(file_name="sample.txt"):
	data = {}
	with open(file_name, 'r') as f:
		for line in f:                 #iterating file 
			words = cleanwords(line)
			for word in words:
				if data.get(word):
					data[word]+=1     #add counts fo word
				else:
					data[word]=1
	return data
