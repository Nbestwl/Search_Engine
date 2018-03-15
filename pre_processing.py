# This file does all the pre-processing procedures for the html documents
# 1. remove all the html tags
# 2. convert all words into lowercase
# 3. implement a stop list to remove all stop words
# 4. reduce all words down to its stem using its stemmer

from nltk.stem import *
from nltk.stem.porter import *		#import porter stemmer
from nltk.corpus import stopwords 		#nltk is the third party library we are using for stop words and stems.

# Shaina's code start here

# HTML tag removal


# convert all words to lowercase


# ------------------------------Lei's code start here------------------------------
# step 3: remove all stop words from documents
def stopword_removal(sentence):
	# create a stop word instance
	stopWords = set(stopwords.words('english'))
	# strips all stop words from the sentence
	words_after_removal =  [i for i in sentence.lower().split() if i not in stopWords]
	# return the sentence after stop words removal
	return words_after_removal

# step 4: implement a stemmer
def stemmer(sentence):
	ps = PorterStemmer()
	sentence_stemmed = []
	# apply porter stemmer to all words in the sentence
	for words in sentence:
		sentence_stemmed.append(ps.stem(words))
	# return the stemmed sentence
	return sentence_stemmed

# def main():
# 	# this is the example sentence, can be replaced later with stripped html tag documents
# 	sentence = "EECS graduates work everywhere from Fortune 500 companies and small startups to research organizations and academic. Organizations value our students for their strong foundation, hand-on laboratory experience and critical thinking skills. Dedicated faculty members mentor students and help them prepare for future success. Advanced courses and research projects sharpen students' problem solving and communication skills"
# 	# remove stop words first then stem the words
# 	words_no_stopwords = stopword_removal(sentence)
# 	result = stemmer(words_no_stopwords)

# 	# testing
# 	print result

# if __name__ == "__main__":
# 	main()
