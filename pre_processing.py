# This file does all the pre-processing procedures for the html documents
# 1. remove all the html tags
# 2. convert all words into lowercase
# 3. implement a stop list to remove all stop words
# 4. reduce all words down to its stem using its stemmer

from nltk.stem import *
#import porter stemmer
from nltk.stem.porter import *
#nltk is the third party library we are using for stop words and stems.
from nltk.corpus import stopwords
import os
# imported for tag removal
import re


# helper function for stripping all html tags
def cleanhtml(raw_html):
	cleantext = re.sub(r'<[^>]*?>|<script[^script>]+>', '', raw_html)
	return cleantext

# remove all html tags from a targeted firectory
def tag_removal():
	print "\nstart removing tags...\n"
	# read in the sample files directory
	rootdir = '/Users/silencer/Desktop/workspace/ir_project/EECS-767/docsnew/'
	# initilize an empty list to store all testing strings
	docs = list()
	# loop through all test files in the dir and assign file contents to a variable
	for subdir, dirs, files in os.walk(rootdir):
		file_path = os.path.join(subdir, files[1])
		with open(file_path, "r") as myfile:
			doc = myfile.read()
			# add the document to docs one at a time
			docs.append(cleanhtml(doc))


	# return the list containing all documents
	return docs

# converting all to lowercase
def case_convention():
	print "\nstart converting to lowercases...\n"


# step 3: remove all stop words from documents
def stopword_removal(sentence):
	# create a stop word instance
	stopWords = set(stopwords.words('english'))
	# strips all stop words from the sentence
	words_after_removal =  [i for i in sentence.lower().split() if i not in stopWords]
	# return the sentence after stop words removal
	return words_after_removal

# step 4: implement a stemmer
def stemmer(sentence):
	ps = PorterStemmer()
	sentence_stemmed = []
	# apply porter stemmer to all words in the sentence
	for words in sentence:
		sentence_stemmed.append(ps.stem(words))
	# return the stemmed sentence
	return sentence_stemmed
