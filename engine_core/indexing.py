# This file takes in all the pre-processed documents as input and it
# will build an inverted index for the documents
# 1.store all documents in a dictionary structure
# 2.ceate a posting list for each row in the dictionary and connect to its index
# 3.testing it within a folder that contains a number of files

import time
import os
from pre_processing import progressbar, tag_removal, stopword_removal, stemmer
from engine_core.linkedList import LinkedList
from multiprocessing import Pool


"""
	pre: document lists
	post: removing stop words and stmmers
	return: doc lists
"""
def preproecssing_helper(docs):
	processed_docs = []
	# remove stopwords
	doc_no_stopwords = stopword_removal(docs)
	# stemming the words
	doc_stemmer = stemmer(doc_no_stopwords)
	processed_docs.append(doc_stemmer)

	return processed_docs


"""
	pre: dictionary(list), postings(list)
	post: print a table for dictionary and be able to adjust the width of term column, printposting lists according to terms
	return: NONE
"""
def print_table(dictionary, postings):
	# calculate the longest string length
	width = 0

	for row in dictionary:
		if len(row['term']) > width:
			width = len(row['term'])

	# start printing dictionary
	print "\n\n-------------Dictionary-------------"
	# using the length of the longest string as the column width
	print "{0:<{3}} {1:<{4}} {2:<{5}}".format('Term','Doc_freq','Term_freq', width, 10, 10)
	for row in dictionary:
		print "{0:<{3}} {1:<{4}} {2:<{5}}".format(row["term"], row["doc_freq"], row["term_freq"], width, 10, 10)

	# start printing posting lists
	print "\n\n-------------Postings-------------"
	# print posting lists
	for posting in postings:
		posting.printList()


"""
	pre: a list of preprocessed documents, a unique word list
	post: create a dictionary, pass in a list containing list of docs, and a list of all words
	return: dictionary, posting list
"""
def postingLists_creation(docs, unique_words):
	dictionary, postings, row = [], [], {}

	# sort the unique words in alphabetical order
	unique_words =  ' '.join(unique_words).split()
	unique_words.sort()

	# print unique_words
	for i, unique_word in enumerate(unique_words):
		total = len(unique_words)
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
		progressbar(i + 1, total, prefix = 'Building dictionary and posting lists:', length = 50)

	return dictionary, postings


"""
	pre: a list of docs, a list of doc filenames
	post: this is the main function to export
	return: dictionary, posting lists
"""
def indexing(docs):
	# variable initialization
	processed_docs, doc_list, unique_words, async_result = [], [], [], []

	# using multi thread to pre process all the documents
	p = Pool(processes=8)
	result = p.map(preproecssing_helper, docs)
	# flatten the list
	processed_docs = [item for sublist in result for item in sublist]

	# load in all docs into a list structure and flat out the nested list
	for doc in processed_docs:
		for word in doc:
			doc_list.append(word)
	# find all the words without duplicates
	[unique_words.append(x) for x in doc_list if x not in unique_words]

	# create a ditionary and a postings list for pre-processed documents
	dictionary, postings = postingLists_creation(processed_docs, unique_words)

	return  dictionary, postings


