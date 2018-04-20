# This file comtains all the procedures to calcualte tf-idf similarity scores between query and each doc
# TODO:
# 1.calculate the length of the corresponding doc vector for each doc
# 2.pre-process the query and calc the length of query vector
# 3.compute the tf-idf similarity scores

from indexing import indexing
from LinkedList import *
from decimal import *
from math import log10
import numpy as np


"""
	pre: numpy array
	post: helper function for writing data into a txt file
	return: NONE
"""
def write_data(weight_matrix):
	np.savetxt('weight_matrix.txt', weight_matrix, fmt='%1.3f')


"""
	pre: a vector
	post: this is the helper function for calculating the vector length
	return: vector length
"""
def vector_length_calc(doc_vec):
	total = 0
	for weight in doc_vec:
		total += weight ** 2
	return total ** 0.5


"""
	pre: d1 is a normalized list, d2 is a normalized list
	post: calculate the cosine similarity
	return: similarity score
"""
def cos_sim(d1, d2):
	result = map(lambda n1, n2: n1 * n2, d1, d2)
	return sum(result)


"""
	pre: dictionary(list), posting(list), filenames(list)
	post: creates a TF_IDF weight matrix using pre-processed dictionary and posting lists
	return: tf-idf weight matrix
"""
def tf_idf(dictionary, postings, filenames):
	# get the number of the documents, which is N in idf
	N = len(filenames)
	rows = len(dictionary)

	# initialize weight matrix with 0s
	weight_matrix = np.zeros(shape=(rows, N + 1), dtype=np.float)
	# calculate idf
	for i in range(len(dictionary)):
		df = dictionary[i]['doc_freq']
		# calculate idf
		idf = log10(Decimal(N)/Decimal(df))
		weight_matrix[i, 0] = idf
		# scan through posting lists to load in the term freq
		for j in range(N):
			# the term exists in the doc then load in the term freq
			if postings[i].find(j):
				weight_matrix[i, j + 1] = postings[i].find(j) * idf
			# it will be 0 if it doesn't exist
			else:
				weight_matrix[i, j + 1] = 0

	# return the tf-idf weight matrix
	print weight_matrix
	return weight_matrix


"""
	pre: a weight matrix(numpy array)
	post: calculating vector length for each document
	return: list of vector length of each columns
"""
def vector_length(weight_matrix):
	doc_vec_length_list = list()
	for i in range(1, weight_matrix.shape[1]):
		vec_len = vector_length_calc(weight_matrix[:, i])
		doc_vec_length_list.append(vec_len)

	return doc_vec_length_list


"""
	pre: query from the user input, dictionary(list), weight_matrix(numpy array), filenames(list)
	post: pre-processing the query
	return: a tuple contains ranking score, doc name, index
"""
def query_processing(query, dictionary, weight_matrix, filenames):
	# creates a list for document candidate
	relevant_doc, normalized_weight, normalized_query, indexes = list(), list(), list(), list()

	query_weight = [0] * len(dictionary)
	# construct the query vector
	for word in query:
		for index, item in enumerate(dictionary):
			if word == item['term']:
				query_weight[index] = weight_matrix[index, 0]

	# if the query contains no relevant words, then output a msg and ask user to input again
	if all(v == 0 for v in query_weight):
		print 'nothing is found'
		return False
	else:
		# identify all the document candidates
		for col in range(weight_matrix[:, 1:].shape[1]):
			# normalize the weight matrix
			normalized_weight = weight_matrix[:,col + 1] / vector_length(weight_matrix)[col]
			normalized_query = [x / vector_length_calc(query_weight) for x in query_weight]
			# calculate the cosine similarity
			relevance = cos_sim(normalized_weight, normalized_query)
			# if the result does not contain all 0's then it is a relevant doc
			if relevance != 0:
				relevant_doc.append(relevance)
				indexes.append(col)

		# sort the document based on the cosine similarity from highest to the lowest
		# create a tuple contains ranking score, doc name, index
		doc_with_rank_score = zip(relevant_doc, [filenames[i] for i in indexes], indexes)
		doc_with_rank_score = sorted(doc_with_rank_score, key=lambda tup: tup[0], reverse=True)

		print doc_with_rank_score
		return relevant_doc
