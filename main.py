# This is the main file, it will process the documents using customized functions from each file and call everything in here.

from pre_processing import *
from indexing import *

def main():
	print "start pre-processing html tags..."
	print "start buidling dictionary and postings"
	# processed_html = tag_removal()
	# create dictionary and postings
	docs = doc_reader()
	print docs
	dictionary, postings = indexing(docs)
	# testing results
	print_table(dictionary, postings)


if __name__ == '__main__':
	main()

