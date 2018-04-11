# This is the main file, it will process the documents using customized functions from each file and call everything in here.
from pre_processing import *
from indexing import *

def main():
	print "\nstart pre-processing html tags...\n"
	docs, filenames = tag_removal()

	print "\nstart buidling dictionary and postings\n"
	# create dictionary and postingsb
	# docs = doc_reader()
	# print docs
	dictionary, postings = indexing(docs, filenames)
	# testing results
	# print_table(dictionary, postings)


if __name__ == '__main__':
	main()

