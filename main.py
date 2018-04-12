# This is the main file, it will process the documents using customized functions from each file and call everything in here.
from pre_processing import *
from indexing import *
from vector_space_model import tf_idf

def main():
	print "\n\nstart pre-processing html tags..."
	docs, filenames = tag_removal()

	print "\n\nstart buidling dictionary and postings"
	# create dictionary and postingsb
	dictionary, postings = indexing(docs, filenames)
	# testing results
	print_table(dictionary, postings)

	print "\n\nstart building vector space model..."
	tf_idf(dictionary, postings, filenames)


if __name__ == '__main__':
	main()

