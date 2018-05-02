
# This is the main file, it will process the documents using customized functions from each file and call everything in here.
from pre_processing import *
from indexing import *
from vector_space_model import tf_idf
from web_crawler import spider
import json
import pickle


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
	pre: dictionary, postings, idf
	post: helper function for writing data into a txt file
	return: NONE
"""
def write_data(dictionary, postings, idf):
	with open('dictionary.txt', 'w') as filehandle:
		json.dump(dictionary, filehandle)

	with open('postings.pkl', 'wb') as filehandle:  # Overwrites any existing file.
		pickle.dump(postings, filehandle, pickle.HIGHEST_PROTOCOL)

	with open('idf.txt', 'w') as filehandle:
		for i in idf:
			filehandle.write('%s\n' % i)


"""
	pre: NONE
	post: setup the index and related posting lists and idf for future search
	return: NONE
"""
def setup():
	# var init
	posting_list = []

	# limit = 10
	start = time.time()

	# root_url = 'http://www.leiwangcoding.com'
	# spider(root_url, limit)

	print bcolors.BOLD + bcolors.OKGREEN + "\n\nstart pre-processing html tags".upper() + bcolors.ENDC
	docs, filenames = tag_removal()

	print bcolors.BOLD + bcolors.OKGREEN + "\n\nstart buidling dictionary and postings".upper() + bcolors.ENDC
	# create dictionary and postingsb
	dictionary, postings = indexing(docs)

	print_table(dictionary, postings)

	# store posting lists in a dictionary
	for posting in postings:
		posting_list.append(posting.retrive_doc_freq())

	print posting_list


	print bcolors.BOLD + bcolors.OKGREEN + "\n\nstart building vector space model".upper() + bcolors.ENDC
	idf = tf_idf(dictionary, filenames)
	print idf

	end = time.time()
	print 'elapsed time: ', end - start

	write_data(dictionary, postings, idf)


if __name__ == '__main__':
	setup()
