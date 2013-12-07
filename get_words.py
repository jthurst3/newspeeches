# get_words.py
# returns a list of words from the relevant lines of a speech
# J. Hassler Thurston
# RocHack Hackathon December 7, 2013

import csv
import nltk

def get_words(line_list):
	sentences = parse_to_sentences(line_list)
	#print sentences
	words = [nltk.word_tokenize(sent) for sent in sentences]
	return sentences

# returns a list of sentences from the list of lines
def parse_to_sentences(line_list):
	#print line_list
	sentence_list = []
	for line in line_list:
		# insert the sentences into the list
		sentence_list.extend(line.split('.'))
	return sentence_list

# exports the list of words to a CSV file (currently only exports sentences)
def export_to_csv(word_list, filename):
	out = open(filename, 'w')
	#wr = csv.writer(out, quoting=csv.QUOTE_ALL)
	for sentence in word_list:
		out.write(sentence + '\n')
	out.close()