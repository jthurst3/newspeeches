# parser.py
# parses sentences from the CSV files
# J. Hassler Thurston
# RocHack Hackathon December 7, 2013

import nltk

cfg_file = 'upenn_grammar.cfg'
dictionary = []
dictionary_str = []

# returns a list of words in our CFG
def get_dictionary():
	global dictionary, dictionary_str, tbank_grammar
	# from http://stackoverflow.com/questions/7056996/how-do-i-get-a-set-of-grammar-rules-from-penn-treebank-using-python-nltk
	tbank_productions = set(production for sent in nltk.corpus.treebank.parsed_sents()
                        for production in sent.productions())
	tbank_grammar = nltk.grammar.ContextFreeGrammar(nltk.grammar.Nonterminal('S'), list(tbank_productions))
	dictionary = list(tbank_productions)
	dictionary_str = [production.__str__() for production in dictionary]

# adds unknown rules to the dictionary and CSV file
def add_words(csv_file):
	f = open(csv_file, 'r')
	cfg = open(cfg_file, 'a')
	for line in f:
		split = nltk.word_tokenize(line)
		tokens = nltk.pos_tag(split)
		for token in tokens:
			rulestr = make_rule(token)
			if rulestr not in dictionary_str:
				cfg.write(rulestr + '\n')
				dictionary.append(nltk.grammar.Production(token[1], [token[0]]))
				dictionary_str.append(rulestr)
	f.close()
	cfg.close()

# converts a parsed word/POS pair into a rule to be added to the CFG
def make_rule(token):
	nonterminal = token[1]
	terminal = token[0]
	return nonterminal + ' -> \'' + terminal + '\''

# parses sentences in the CSV file
def parse(csv_file):
	f = open(csv_file, 'r')
	cfg = open(cfg_file, 'r')
	cfg_grammar = cfg.read()
	for line in cfg_grammar:
		split = line.split(' -> ')
		if len(split) >= 2:
			dictionary.append(nltk.grammar.Production(split[0], [split[1]]))
	grammar = nltk.grammar.ContextFreeGrammar(nltk.grammar.Nonterminal('S'), dictionary)
	parser = nltk.RecursiveDescentParser(grammar)
	split = nltk.word_tokenize(' Chief Justice, members of the United States Congress, distinguished guests, and fellow citizens:')
	parsed = parser.nbest_parse(split)
	print parsed
	# for line in f:
	# 	split = nltk.word_tokenize(line)
	# 	parsed = parser.nbest_parse(split)
	# 	print parsed
	f.close()
	cfg.close()



