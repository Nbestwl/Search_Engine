# This file does all the pre-processing procedures for the html documents
# 1. remove all the html tags
# 2. convert all words into lowercase
# 3. implement a stop list to remove all stop words
# 4. reduce all words down to its stem using its stemmer

import sys
#import porter stemmer
from stemming.porter2 import stem
#nltk is the third party library we are using for stop words and stems.
from stop_words import get_stop_words
import os
# imported for tag removal
import re


"""
	pre: text(a list of strings)
	post: remove all the html tags
	return: a tag removed document
"""
def process_html(text):
	# remove everything within script and css tags
	scripts = re.compile(r'<(script).*?</\1>(?s)')
	css = re.compile(r'<style.*?/style>')
	# remove all html tags
	tags = re.compile(r'<.*?>')

	# replace all tags with a single space
	text = scripts.sub(' ', text)
	text = css.sub(' ', text)
	text = tags.sub(' ', text)
	# remove all \n and \t in the document
	text = re.sub(r'\n', '', text)
	text = re.sub(r'\t', '', text)
	# remove all non word elements
	non_words = re.compile('[^a-zA-Z]')
	text = non_words.sub(' ', text)

	# converft multiple spaces into a single space
	# remove all single letter
	# convert to lowercase
	return ' '.join([w for w in text.split() if len(w)>1]).lower()


"""
	pre: the current iteration, total iterations, prefix, suffix, length of the bar, fill
	post: construct a progress bar and show the percentage of the progress
	return: NONE
"""
def progressbar(iteration, total, prefix, length, fill=u'\u2588'):
	percent = ("{0:." + str(1) + "f}").format(100 * (iteration / float(total)))
	filledLength = int(length * iteration // total)
	bar = fill * filledLength + ' ' * (length - filledLength)
	suffix = str(iteration) + "/" + str(total)

	sys.stdout.write('%s |%s| %s%% %s\r' % (prefix, bar, percent, suffix))
	sys.stdout.flush()


"""
	pre: NONE
	post: remove all html tags from a targeted firectory
	return: a list of all tag removed docs, a list of filenames
"""
def tag_removal():
	# read in the sample files directory
	rootdir = '/Users/silencer/Desktop/workspace/ir_project/search_engine/engine_core/temp/'
	# initilize an empty list to store all testing strings
	docs = list()
	filenames = list()
	# loop through all test files in the dir and assign file contents to a variable
	for root, dirs, files in os.walk(rootdir):
		total = len(files)
		# sort the file name in order
		for i, file in enumerate(sorted(files)):
			file_path = os.path.join(root, file)
			with open(file_path, "r") as myfile:
				doc = myfile.read()
				# add the document to docs one at a time
				docs.append(process_html(doc))
				progressbar(i + 1, total, prefix = 'Progress:', length = 50)
				filenames.append(file)

	return docs, filenames


"""
	pre: a document
	post: step 3: remove all stop words from documents
	return: a doc with no stopwords
"""
def stopword_removal(doc):
	# create a stop word instance
	stopWords = get_stop_words('en')
	# strips all stop words from the document
	words_after_removal =  [i for i in doc.lower().split() if i not in stopWords]
	# return the document after stop words removal
	return words_after_removal


"""
	pre: a document
	post: step 4: implement a stemmer
	return: a stemmed document
"""
def stemmer(doc):
	sentence_stemmed = []
	# apply porter stemmer to all words in the document
	for words in doc:
		sentence_stemmed.append(stem(words))
	# return the stemmed document
	return sentence_stemmed

