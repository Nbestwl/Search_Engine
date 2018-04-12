# This is the main file, it will process the documents using customized functions from each file and call everything in here.
from pre_processing import *
from indexing import *
from vector_space_model import tf_idf, vector_length, query_processing, vector_length_calc

def main():
	print "\n\nstart pre-processing html tags..."
	docs, filenames = tag_removal()

	print "\n\nstart buidling dictionary and postings"
	# create dictionary and postingsb
	dictionary, postings = indexing(docs, filenames)
	# testing results
	print_table(dictionary, postings)

	print "\n\nstart building vector space model..."
	weight_matrix = tf_idf(dictionary, postings, filenames)

	print "\n\ncalculating document vector length..."
	doc_vec_length_list = vector_length(weight_matrix)
	print doc_vec_length_list

	print "\n\nquery vector length calculation..."
	query = "lei silver truck truck"
	query_weight = query_processing(query, dictionary, weight_matrix)
	print query_weight
	query_vec_length = vector_length_calc(query_weight)
	print query_vec_length

if __name__ == '__main__':
	main()

