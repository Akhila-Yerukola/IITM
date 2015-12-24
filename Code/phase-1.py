import os
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag,map_tag
from collections import OrderedDict

#input_path=os.path.join(os.path.dirname(__file__), '../Cases/Text2pdf.pdf')
output_path=os.path.join(os.path.dirname(__file__), '../Cases/Text1.txt')
#os.system(("pdftotext %s %s") %( input_path , output_path))
input_file=open(output_path,'r')
#print input_file.read()

tag_words=pos_tag(word_tokenize(input_file.read()))
#print tag_words
simplified_text = [(word, str(map_tag('en-ptb', 'universal', tag))) for word, tag in tag_words]
#print simplified_text

res = OrderedDict()
for v, k in simplified_text:
	if k in res:
		if v not in res[k]:
			res[k].append(v)
	else: res[k] = [v]

print res.keys()