# This file comtains all the procedures to calcualte tf-idf similarity scores between query and each doc
# TODO:
# 1.calculate the length of the corresponding doc vector for each doc
# 2.pre-process the query and calc the length of query vector
# 3.compute the tf-idf similarity scores

from indexing import *
from decimal import *
from math import log10


def tf_idf():
	idf, tf_idf, dic_row = [], [], {}
	# get the document list
	docs = doc_reader()
	# get the size of the list, which is N in idf
	N = len(docs)
	# calculate idf
	dictionary, postings = indexing(docs)
	for row in dictionary:
		df = row['term_freq']
		idf.append(log10(Decimal(N)/Decimal(df)))
	# build the weight matrix
	for row in range(0, len(dictionary)):
		dic_row['term'] = dictionary[row]['term']
		postinglist = postings[row]
		for doc_num in range(0, N):
			if postinglist.find(doc_num):
				dic_row[doc_num] = postinglist.find(doc_num) * idf[row]
			else:
				dic_row[doc_num] = 0
		tf_idf.append(dic_row.copy())

	return tf_idf


# def vector_cal(tf_idf):
# 	vector_length = {}

# 	for row in range(0, len(tf_idf)):
# 		for i



def main():
	print "start building vector space model..."
	print tf_idf()


if __name__ == '__main__':
	main()
