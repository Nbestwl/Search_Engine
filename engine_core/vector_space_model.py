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
	pre: d1 is a vector, d2 is a vector
	post: calculate the cosine similarity
	return: similarity score
"""
def cos_sim(d1, d2):
	l1 = vector_length_calc(d1)
	l2 = vector_length_calc(d2)
	result = sum(map(lambda n1, n2: n1 * n2, d1, d2))
	return result / (l1 * l2)


"""
	pre: dictionary(list), filenames(list)
	post: creates a IDF list using pre-processed dictionary and number of files
	return: idf list
"""
def tf_idf(dictionary, filenames):
	# get the number of the documents, which is N in idf
	N = len(filenames)
	rows = len(dictionary)

	# initialize weight matrix with 0s
	# weight_matrix = np.zeros(shape=(rows, N + 1), dtype=np.float)
	# calculate idf
	idf_list = []
	for i in range(len(dictionary)):
		df = dictionary[i]['doc_freq']
		# calculate idf
		idf = log10(Decimal(N)/Decimal(df))
		idf_list.append(idf)

	return idf_list


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

	print 'query_weight: ', query_weight
	# if the query contains no relevant words, then output a msg and ask user to input again
	if all(v == 0 for v in query_weight):
		print 'nothing is found'
		return False
	else:
		# identify all the document candidates
		for col in range(weight_matrix[:, 1:].shape[1]):
			# normalize the weight matrix
			if vector_length(weight_matrix)[col] != 0:
				normalized_weight = weight_matrix[:,col + 1] / vector_length(weight_matrix)[col]
			print 'normalized_weight: ', normalized_weight

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

"""
	pre: query string list, dictionary, posting lists, idf list
	post: using dictionary to match the query index and retrieve doc and freq info from posting lists
	return: ranked documents with cosine similarity
"""
def query_search(query, dictionary, postings, idf):
	# var init
	query_vector = []
	cos_sim_helper = []

	# search the word in the dictionary and locate the index of the word
	for word in query:
		# variable init
		all_docs, all_freq, tf_idf = [], [], []
		for index, item in enumerate(dictionary):
			if word == item['term']:
				# construct the query vector using idf list
				query_vector.append(idf[index])
				# retrieve the document numbers and term frequency of that specific term
				all_docs, all_freq = postings[index].retrive_doc_freq()
				# retrieve the corresponding idf
				tf = idf[index]
				# use idf to calculate the tf-idf
				tf_idf = map(lambda x: x * tf, all_freq)

				# store the tf-idf, doc number and index of the word into a list for futher cosine similarity calc
				for doc in all_docs:
					# add another entry if the doc is not in the list
					if doc not in cos_sim_helper:
						cos_sim_helper.append(doc)

		print all_docs, tf_idf
	print 'query_vector: ', query_vector
	print 'cos_sim_helper: ', cos_sim_helper


def main():
	v1 = [0.12493873660829993, 12493873660829993]
	v2 = [0.12493873660829993, 12493873660829993]

	print cos_sim(v1, v2)


if __name__ == '__main__':
	main()
