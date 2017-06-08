from trantor_clean_words import cleanwords

def noise_words(file_path="sample.txt", noise_limit =3):#noise limit is allowed count of a word defaut 3
	data = {}
	with open(file_path, 'r') as f:
		for line in f:
			words = cleanwords(line)
			for i in range(1,len(words)):
				pair = (words[i-1],words[i])
				if data.get(pair):
					data[pair]+=1     #add counts fo word
					if data[pair] > noise_limit:
						del data[pair]
				else:
					data[pair]=1
	return data

