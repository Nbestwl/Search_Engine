
# This is the main file, it will process the documents using customized functions from each file and call everything in here.
import sys
from pre_processing import *
from indexing import *
from vector_space_model import tf_idf, vector_length, query_processing, vector_length_calc, write_data, query_search
from web_crawler import spider


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
	limit = 10
	start = time.time()

	root_url = 'http://www.leiwangcoding.com'
	spider(root_url, limit)

	print bcolors.BOLD + bcolors.OKGREEN + "\n\nstart pre-processing html tags".upper() + bcolors.ENDC
	docs, filenames = tag_removal()

	print bcolors.BOLD + bcolors.OKGREEN + "\n\nstart buidling dictionary and postings".upper() + bcolors.ENDC
	# create dictionary and postingsb
	dictionary, postings = indexing(docs)
	# testing results
	# print_table(dictionary, postings)

	print bcolors.BOLD + bcolors.OKGREEN + "\n\nstart building vector space model".upper() + bcolors.ENDC
	idf = tf_idf(dictionary, filenames)

	# writing all the weight matrix to a single file
	# print bcolors.BOLD + bcolors.OKGREEN + "\n\nwriting data to a file".upper() + bcolors.ENDC
	# write_data(weight_matrix)

	end = time.time()
	print 'elapsed time: ', end - start

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
		similarity_score = query_search(processed_query, dictionary, postings, idf, filenames)

if __name__ == '__main__':
	main()

