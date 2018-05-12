import json
import pickle
import os.path
import numpy as np
from setup import bcolors
from pre_processing import *
from indexing import print_table
from engine_core.linkedList import LinkedList
from vector_space_model import query_search
from web_crawler import read_title_from
import time

"""
	pre: NONE
	post: helper function for reading data from a txt file
	return: dictionary, postings, idf in lists
"""
def read_data():
	dictionary, postings_list, idf, urls = [], [], [], []

	abusolute_path = os.path.abspath(os.path.dirname(__file__))
	# reading dictionary to a list
   	with open(abusolute_path+'/dictionary.txt') as f:
   		dictionary = json.load(f)
   	# reading postings to a list
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

	# retrieve urls
	with open(abusolute_path+'/urls.txt') as filehandle:
		for i in filehandle:
			urls.append(i)

	return dictionary, postings_list, idf, urls


"""
	pre: query string
	post: this method is for UI intergration
	return: similarity score
"""
def search(query):
	# var init
	dictionary, postings, idf, urls, title = [], [], [], [], []
	# reading all index data from files
	dictionary, postings, idf, urls = read_data()

	start = time.time()
	processed_query = stopword_removal(query)
	processed_query = stemmer(processed_query)
	similarity_score = query_search(processed_query, dictionary, postings, idf, urls)

	return similarity_score
	end = time.time()
	print 'elapsed time: ', end - start


"""
	pre: query string from web UI
	post: sompare the query and calc the cosine similarity to get the relevant docs
	return: a list of relevant docs
"""
def main():
	# var init
	dictionary, postings, idf, urls, title = [], [], [], [], []
	# reading all index data from files
	dictionary, postings, idf, urls = read_data()

	print_table(dictionary, postings)

	while True:
		query = raw_input(bcolors.BOLD + bcolors.OKGREEN + '\n\nEnter your query to search:(type q to quit search) \n'.upper() + bcolors.ENDC).lower()
		if query == 'q':
			print "goodbye!"
			exit()
		else:
			start = time.time()
			print bcolors.BOLD + bcolors.OKGREEN + "\n\ncalculating document rankings".upper() + bcolors.ENDC
			processed_query = stopword_removal(query)
			processed_query = stemmer(processed_query)

		# similarity_score = query_processing(processed_query, dictionary, weight_matrix, filenames)
		similarity_score = query_search(processed_query, dictionary, postings, idf, urls)
		print similarity_score
		end = time.time()
		print 'elapsed time: ', end - start


if __name__ == '__main__':
	main()


