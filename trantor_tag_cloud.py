import webbrowser
from trantor_word_freq import wordfreq

def tag_cloud(file_path="sample.txt"):# input file path for parsing
	data = wordfreq(file_path)
	with open('cloud_tag.html', 'w') as f:# html file with tag
		for k,v  in sorted(data.items()):
			f.write('<a href="{}" style="font-size: {}px;">{}</a><br>'.format(k, 4*v,k)) # generating cloudtags

	webbrowser.open('file://' + os.path.realpath('cloud_tag.html'))