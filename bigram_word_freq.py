from trantor_clean_words import cleanwords

def wordfreq(file_name="sample.txt"):
	data = {}
	with open(file_name, 'r') as f:
		for line in f:                 #iterating file 
			words = cleanwords(line)
			for i in range(1,len(words)):
				pair = (words[i-1],words[i])
				if data.get(pair):
					data[pair]+=1     #add counts fo word
				else:
					data[pair]=1
	return data
