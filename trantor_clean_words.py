import string

def cleanwords(text):
	clean_list = []
	words = text.split()
	for word in words:
		# could have used translate(faster) instead inbult method to remove punctuation
		# word.translate(string.maketrans("",""), string.punctuation)
		word = ''.join([char for char in word if char not in string.punctuation])
		try:
			int(word)
		except ValueError:
			clean_list.append(word.lower())
	return clean_list

