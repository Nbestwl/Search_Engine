# This is the main file, it will process the documents using customized functions from each file and call everything in here.
from pre_processing import *
from indexing import *

def main():
	# initialization
	filenames = list()

	print "start pre-processing html tags..."
	docs = tag_removal()

	# print docs
	# filenames = directory_info()
	# progress(filenames)

	# print "start buidling dictionary and postings"
	# # create dictionary and postingsb
	# docs = doc_reader()
	# print docs
	# dictionary, postings = indexing(docs)
	# # testing results
	# print_table(dictionary, postings)


if __name__ == '__main__':
	main()

