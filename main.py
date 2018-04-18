
# This is the main file, it will process the documents using customized functions from each file and call everything in here.
import sys
from pre_processing import *
from indexing import *
from vector_space_model import tf_idf, vector_length, query_processing, vector_length_calc


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


"""
	pre: NONE
	post: main function putting everything together
	return: NONE
"""
def main():
	print bcolors.BOLD + bcolors.OKGREEN + "\n\nstart pre-processing html tags...".upper() + bcolors.ENDC
	docs, filenames = tag_removal()

	print bcolors.BOLD + bcolors.OKGREEN + "\n\nstart buidling dictionary and postings".upper() + bcolors.ENDC
	# create dictionary and postingsb
	dictionary, postings = indexing(docs)
	# testing results
	# print_table(dictionary, postings)

	print bcolors.BOLD + bcolors.OKGREEN + "\n\nstart building vector space model...".upper() + bcolors.ENDC
	weight_matrix = tf_idf(dictionary, postings, filenames)

	print bcolors.BOLD + bcolors.OKGREEN + "\n\ncalculating document rankings...".upper() + bcolors.ENDC
	query = "damaged"

	processed_query = stopword_removal(query)
	processed_query = stemmer(processed_query)

	similarity_score = query_processing(processed_query, dictionary, weight_matrix, filenames)

if __name__ == '__main__':
	main()

