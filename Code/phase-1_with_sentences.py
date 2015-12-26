import os
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.tag import pos_tag,map_tag
from collections import OrderedDict
from nltk.stem.porter import *
#from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords

# Run only the fisrt time to convert pdf to txt : Might introduce junk chars

#input_path=os.path.join(os.path.dirname(__file__), '../Cases/Text2pdf.pdf')
output_path=os.path.join(os.path.dirname(__file__), '../Cases/Text1.txt')

#os.system(("pdftotext %s %s") %( input_path , output_path))

###############################################################################
# Contruction of tag words
###############################################################################

with open(output_path,'r') as input_file:
	sentences=sent_tokenize(input_file.read())
	#tag_words=pos_tag(word_tokenize(input_file.read()))

sentences=[word_tokenize(sent) for sent in sentences]
sentences=[pos_tag(sent) for sent in sentences]
sentences_new=[]
for sent in sentences:
	sent_new=[(word.lower(), str(map_tag('en-ptb', 'universal', tag)).lower()) for word, tag in sent]
	sentences_new.append(sent_new)

#sentences=[(word.lower(), str(map_tag('en-ptb','universal',tag)).lower()) for sent in sentences for word,tag in sent ]
#print sentences_new
#simplified_text = [(word.lower(), str(map_tag('en-ptb', 'universal', tag)).lower()) for word, tag in tag_words]

###############################################################################
# Removing stop words
###############################################################################

cached_stopwords = stopwords.words('english')
cached_stopwords = [str(word) for word in cached_stopwords]
text_removed_stopwords = []
sent_removed_tagwords=[]
for sent in sentences_new:
	text_removed_stopwords = []
	for k,v in sent:
		if k not in cached_stopwords and v!='.':
			t=(k,v)
			text_removed_stopwords.append(t)
	sent_removed_tagwords.append(text_removed_stopwords)


#print sent_removed_tagwords

#res = OrderedDict()
#for v, k in simplified_text:
#	if k in res:
#		if v not in res[k]:
#			res[k].append(v)
#	else: res[k] = [v]


###############################################################################
# Porter Stemming
###############################################################################

stemmer = PorterStemmer()
#lemmatizer = WordNetLemmatizer()
#stemmed_words=[ (str(stemmer.stem(k)),v) for k,v in text_removed_stopwords]
stemmed_sentences=[ [(str(stemmer.stem(k)),v) for k,v in sent] for sent in sent_removed_tagwords]
print stemmed_sentences
#print [lemmatizer.lemmatize(t) for t in res['VERB']]

###############################################################################
# Construction of tagged corpus
###############################################################################

output_path=os.path.join(os.path.dirname(__file__), '../Cases/')
with open(os.path.join(output_path, 'TaggedText1.txt'), 'w') as tagged_file:
	tagged_file.writelines("%s/%s " % (k,v) for sent in stemmed_sentences for k,v in sent )
with open(os.path.join(output_path, 'ProcessedText1.txt'), 'w') as tagged_file:
	tagged_file.writelines("%s " % k for sent in stemmed_sentences for k,v in sent )
with open(os.path.join(output_path, 'ProcessedText1_no_stem.txt'), 'w') as tagged_file:
	tagged_file.writelines("%s " % k for sent in sent_removed_tagwords for k,v in sent)


###############################################################################
# Grouping of words to form synsets
###############################################################################



