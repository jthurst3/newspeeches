# parser.py
# parses sentences from the CSV files
# J. Hassler Thurston
# RocHack Hackathon December 7, 2013

import nltk

cfg_file = 'upenn_grammar.cfg'
dictionary = []

# returns a list of words in our CFG
def get_dictionary():
	global dictionary
	cfg = open(cfg_file, 'r')
	dictionary = cfg.read().split('\n')
	cfg.close()

# adds unknown rules to the dictionary and CSV file
def add_words(csv_file):
	f = open(csv_file, 'r')
	cfg = open(cfg_file, 'a')
	for line in f:
		split = nltk.word_tokenize(line)
		tokens = nltk.pos_tag(split)
		for token in tokens:
			rulestr = make_rule(token)
			if rulestr not in dictionary:
				cfg.write(rulestr + '\n')
				dictionary.append(rulestr)
	f.close()
	cfg.close()

# converts a parsed word/POS pair into a rule to be added to the CFG
def make_rule(token):
	nonterminal = token[1]
	terminal = token[0]
	return nonterminal + ' -> \'' + terminal + '\''