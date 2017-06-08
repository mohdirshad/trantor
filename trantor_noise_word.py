from trantor_clean_words import cleanwords

def noise_words(file_path="sample.txt", noise_limit =3):#noise limit is allowed count of a word defaut 3
	data = {}
	with open(file_path, 'r') as f:
		for line in f:
			words = cleanwords(line)
			for word in words:
				if data.get(word):
					data[word]+=1
					if data[word] > noise_limit:
						del data[word]   # eleminatig noise word
				else:
					data[word]=1
	return data

