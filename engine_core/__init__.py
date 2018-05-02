import json
import pickle
import os.path
import numpy as np
from setup import bcolors
from pre_processing import *
from indexing import print_table
from engine_core.linkedList import LinkedList
from vector_space_model import query_search


"""
	pre: NONE
	post: helper function for reading data from a txt file
	return: dictionary, postings, idf in lists
"""
def read_data():
	dictionary, postings_list, idf = [], [], []

	abusolute_path = os.path.abspath(os.path.dirname(__file__))
	# reading dictionary to a list
   	with open(abusolute_path+'/dictionary.txt') as f:
   		dictionary = json.load(f)
   	# reading postings to a list
   	# with open(abusolute_path+'/postings.pkl', 'rb') as input:
   	# 	postings = pickle.loads(input)
   	# 	for posting in postings:
  		# 	postings_list.append(posting)

	with open(abusolute_path+'/postings.pkl', 'rb') as input:
	    while True:
	        try:
	            postings_list = pickle.load(input)
	        except EOFError:
	            break
  	# reading idf to a list
	with open(abusolute_path+'/idf.txt') as filehandle:
		for line in filehandle:
			idf.append(float(line))

	return dictionary, postings_list, idf


"""
	pre: query string
	post: this method is for UI intergration
	return: similarity score
"""
def search(query):
	# var init
	dictionary, postings, idf = [], [], []
	# reading all index data from files
	dictionary, postings, idf = read_data()

	processed_query = stopword_removal(query)
	processed_query = stemmer(processed_query)
	similarity_score = query_search(processed_query, dictionary, postings, idf)
	return similarity_score


"""
	pre: query string from web UI
	post: sompare the query and calc the cosine similarity to get the relevant docs
	return: a list of relevant docs
"""
def main():
	# var init
	dictionary, postings, idf = [], [], []
	# reading all index data from files
	dictionary, postings, idf = read_data()

	print_table(dictionary, postings)

	while True:
		query = raw_input(bcolors.BOLD + bcolors.OKGREEN + '\n\nEnter your query to search:(type q to quit search) \n'.upper() + bcolors.ENDC).lower()
		if query == 'q':
			print "goodbye!"
			exit()
		else:
			print bcolors.BOLD + bcolors.OKGREEN + "\n\ncalculating document rankings".upper() + bcolors.ENDC
			processed_query = stopword_removal(query)
			processed_query = stemmer(processed_query)

		# similarity_score = query_processing(processed_query, dictionary, weight_matrix, filenames)
		similarity_score = query_search(processed_query, dictionary, postings, idf)
		print similarity_score



if __name__ == '__main__':
	main()
