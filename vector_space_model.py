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


# this is the helper function for calculating the vector length
def vector_length_calc(doc_vec):
	total = 0
	for weight in doc_vec:
		total += weight ** 2
	return total ** 0.5

# creates a TF_IDF weight matrix using pre-processed dictionary and posting lists
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


# calculating vector length for each document
def vector_length(weight_matrix):
	doc_vec_length_list = list()
	for i in range(1, weight_matrix.shape[1]):
		vec_len = vector_length_calc(weight_matrix[:, i])
		doc_vec_length_list.append(vec_len)

	return doc_vec_length_list


# pre-processing the query
def query_processing(query, dictionary, weight_matrix):
	query_weight = list()
	for word in query:
		for i in range(len(dictionary)):
			term = dictionary[i]['term']
			if word == term:
				query_weight.append(weight_matrix[i, 0])

	return query_weight
