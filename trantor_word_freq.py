from trantor_word_freq import cleanwords

def wordfreq(file_name):
	data = {}
	with open(file_name, 'r') as f:
		for line in f:
			words = cleanwords(line)
			for word in words:
				if data.get(word):
					data[word]+=1
				else:
					data[word]=1
	return data


