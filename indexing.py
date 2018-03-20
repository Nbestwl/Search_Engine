# This file takes in all the pre-processed documents as input and it
# will build an inverted index for the documents
# 1.store all documents in a dictionary structure
# 2.ceate a posting list for each row in the dictionary and connect to its index
# 3.testing it within a folder that contains a number of files

import os
from pre_processing import *
from LinkedList import LinkedList

# create a testing folder that contains files, and be able to load in the text to the pre-processing functions
# return a list of testing strings
def doc_reader():
	# read in the sample files directory
	rootdir = '/Users/silencer/Desktop/workspace/ir_project/EECS-767/testing'
	# initilize an empty list to store all testing strings
	docs = list()
	# loop through all test files in the dir and assign file contents to a variable
	for subdir, dirs, files in os.walk(rootdir):
	    for file in files:
	        file_path = os.path.join(subdir, file)
	        with open(file_path, "r") as myfile:
	        	doc = myfile.read()
	        	# add the document to docs one at a time
	        	docs.append(doc)

	# return the list containing all documents
	return docs


# print a table for dictionary and be able to adjust the width of term column
# print posting lists according to terms
def print_table(dictionary, postings):
	# calculate the longest string length
	width = 0

	for row in dictionary:
		if len(row['term']) > width:
			width = len(row['term'])

	# start printing dictionary
	print "-------------Dictionary-------------"
	# using the length of the longest string as the column width
	print "{0:<{3}} {1:<{4}} {2:<{5}}".format('Term','Doc_freq','Term_freq', width, 10, 10)
	for row in dictionary:
		print "{0:<{3}} {1:<{4}} {2:<{5}}".format(row["term"], row["doc_freq"], row["term_freq"], width, 10, 10)

	# start printing posting lists
	print "-------------Postings-------------"
	# print posting lists
	for posting in postings:
		posting.printList()


# create a dictionary
# pass in a list containing list of docs, and a list of all words
def postingLists_creation(docs, unique_words):
	dictionary, postings, row = [], [], {}

	# sort the unique words in alphabetical order
	unique_words =  ' '.join(unique_words).split()
	unique_words.sort()

	# print unique_words
	for unique_word in unique_words:
		row["term"] = unique_word
		row["doc_freq"] = 0
		row["term_freq"] = 0

		# initialize the linked list for each dictionary columns
		posting = LinkedList()
		for doc in docs:
			occurence = doc.count(unique_word)
			# if the unique word exists in the doc, update freq and linked list
			if occurence > 0:
				row["doc_freq"] += 1
				row["term_freq"] += occurence

				# create a linkedlist and insert doc number and term frequency
				doc_num = docs.index(doc)
				posting.add(doc_num, occurence)
		# append posting list and dictionary for each term
		postings.append(posting)
		dictionary.append(row.copy())

	return dictionary, postings

# this is the main function to export
def indexing(docs):
	# remove stop words first then stem the words
	# docs = doc_reader()
	# pre-processing one document at a time
	processed_docs, doc_list, unique_words, flat_list = [], [], [], []

	for doc in docs:
		# remove stopwords
		doc_no_stopwords = stopword_removal(doc)
		# stemming the words
		doc_stemmer = stemmer(doc_no_stopwords)
		processed_docs.append(doc_stemmer)

	# load in all docs into a list structure and flat out the nested list
	for doc in processed_docs:
		for word in doc:
			doc_list.append(word)

	# find all the words without duplicates
	[unique_words.append(x) for x in doc_list if x not in unique_words]
	# create a ditionary and a postings list for pre-processed documents
	dictionary, postings = postingLists_creation(processed_docs, unique_words)

	return  dictionary, postings
