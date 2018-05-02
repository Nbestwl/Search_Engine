from pre_processing import *
from indexing import print_table
from vector_space_model import query_search
from setup import bcolors
import json
from LinkedList import LinkedList
import numpy as np
import pickle


"""
	pre: NONE
	post: helper function for reading data from a txt file
	return: dictionary, postings, idf in lists
"""
def read_data():
	dictionary, postings_list, idf = [], [], []
	# reading dictionary to a list
   	dictionary = json.load(open('dictionary.txt'))
   	# reading postings to a list
   	with open('postings.pkl', 'rb') as input:
   		postings = pickle.load(input)
   		for posting in postings:
  			postings_list.append(posting)
  	# reading idf to a list
	with open("idf.txt") as filehandle:
		for line in filehandle:
			idf.append(float(line))

	return dictionary, postings_list, idf


"""
	pre: query string from web UI
	post: sompare the query and calc the cosine similarity to get the relevant docs
	return: a list of relevant docs
"""
def search():
	# var init
	dictionary, postings, idf = [], [], []
	# reading all index data from files
	dictionary, postings, idf = read_data()

	# print_table(dictionary, postings)

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



if __name__ == '__main__':
	search()
