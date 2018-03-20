# This is the main file, it will process the documents using customized functions from each file and call everything in here.

from pre_processing import *
from indexing import *

def main():
	print "start pre-processing html tags..."
	processed_html = tag_removal()
	# create dictionary and postings
	dictionary, postings = indexing(processed_html)
	# testing results
	print_table(dictionary, postings)


if __name__ == '__main__':
	main()

