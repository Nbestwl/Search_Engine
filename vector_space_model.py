# This file comtains all the procedures to calcualte tf-idf similarity scores between query and each doc
# TODO:
# 1.calculate the length of the corresponding doc vector for each doc
# 2.pre-process the query and calc the length of query vector
# 3.compute the tf-idf similarity scores

from indexing import doc_reader, indexing
from LinkedList import *
from decimal import *
from math import log10
import numpy as np


# creates a TF_IDF weight matrix using pre-processed dictionary and posting lists
def tf_idf(dictionary, postings, filenames):
	# get the number of the documents, which is N in idf
	N = len(filenames)
	rows = len(dictionary)

	# initialize weight matrix with 0s
	weight_matrix = np.zeros(shape=(rows, N + 1), dtype=np.int)
	# calculate idf
	for i in range(len(dictionary)):
		df = dictionary[i]['doc_freq']
		weight_matrix[i, 0] = df
		# scan through posting lists to load in the term freq
		for j in range(N):
			# the term exists in the doc then load in the term freq
			if postings[i].find(j):
				weight_matrix[i, j + 1] = postings[i].find(j)
			# it will be 0 if it doesn't exist
			else:
				weight_matrix[i, j + 1] = 0

	print weight_matrix
		# idf.append(log10(Decimal(N)/Decimal(df)))
	# # build the weight matrix
	# for row in range(0, len(dictionary)):
	# 	dic_row['term'] = dictionary[row]['term']
	# 	postinglist = postings[row]
	# 	for doc_num in range(0, N):
	# 		if postinglist.find(doc_num):
	# 			dic_row[doc_num] = postinglist.find(doc_num) * idf[row]
	# 		else:
	# 			dic_row[doc_num] = 0
	# 	tf_idf.append(dic_row.copy())

	# # this dictionary will store all document vector length
	# vector_length = {}

	# for row in range(0, len(tf_idf)):
	# 	# for i in range()
	# 	print tf_idf[row][0]


# def main():
# 	print "start building vector space model..."
# 	tf_idf()


# if __name__ == '__main__':
# 	main()
