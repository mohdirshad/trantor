import os
import webbrowser
from trantor_clean_words import cleanwords

def wordlines(file_path="sample.txt"):
	data = {}
	with open(file_path, 'r') as f:
		for number,line in enumerate(f): #enumerate to get the line number
			words = cleanwords(line)
			for i in range(1,len(words)):
				pair = (words[i-1],words[i])
				formated_line = "{} {}".format(number,line)
				if data.get(pair):
					data[pair].append(formated_line)
				else:
					data[pair]=[formated_line]
	return data



def linked_cloud(file_path="sample.txt"):# input file path for parsing
	data = wordlines(file_path)
	cwd = os	.getcwd()
	new_dir = cwd + "/linked"
	if not os.path.exists(new_dir):
		os.makedirs(new_dir)#   making new director for word files to store line
	with open('cloud_tag.html', 'w') as f:# html file with tag
		for word,lines  in sorted(data.items()): # sorting tag in alphanumeric order
		    link = word[0]+word[1]
			f.write('<a href='+"linked/{}.html".format(link)+' style="font-size: 12px;">{}</a><br>'.format(word))
			with open('linked/{}.html'.format(link), 'w') as wordfile:
				for line in lines:
					wordfile.write(line+"<br>")   #writing lines of a word

	webbrowser.open('file://' + os.path.realpath('cloud_tag.html'))