# This is the main file, it will process the documents using customized functions from each file and call everything in here.

from pre_processing import *
from indexing import *

def main():
	print "start building vector space model..."

	print tag_removal()

if __name__ == '__main__':
	main()
