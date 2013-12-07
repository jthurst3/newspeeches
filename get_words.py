# get_words.py
# returns a list of words from the relevant lines of a speech
# J. Hassler Thurston
# RocHack Hackathon December 7, 2013

def get_words(line_list):
	sentences = parse_to_sentences(line_list)
	print sentences
	words = [sent.split(' ') for sent in sentences]
	return words

# returns a list of sentences from the list of lines
def parse_to_sentences(line_list):
	#print line_list
	sentence_list = []
	for line in line_list:
		# insert the sentences into the list
		sentence_list.extend(line.split('.'))
	return sentence_list