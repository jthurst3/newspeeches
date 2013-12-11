# parser2.py
# parses sentences from the CSV files
# J. Hassler Thurston
# RocHack Hackathon December 7, 2013
# Modified December 11, 2013

import nltk
from random import choice

cfg_file = 'upenn_grammar.cfg'
tbank_productions = []
nonterminals = []
rightside = []

def get_initial_rules():
	global tbank_productions, nonterminals
	# from http://stackoverflow.com/questions/7056996/how-do-i-get-a-set-of-grammar-rules-from-penn-treebank-using-python-nltk
	tbank_productions = [production for sent in nltk.corpus.treebank.parsed_sents() for production in sent.productions()]
	nonterminals = [production.lhs().__str__() for production in tbank_productions]
	rightside = [production.rhs().__str__() for production in tbank_productions]
	tbank_grammar = nltk.grammar.ContextFreeGrammar(nltk.grammar.Nonterminal('S'), tbank_productions)
	print generate_sample(tbank_grammar)

# modified from http://stackoverflow.com/questions/15009656/how-to-use-nltk-to-generate-sentences-from-an-induced-grammar
def generate_sample(grammar, items=[nltk.grammar.Nonterminal('S')]):
	frags = []
	if len(items) == 1:
		print items
		if isinstance(items[0], nltk.grammar.Nonterminal):
			frags.append(generate_sample(grammar, grammar.productions(lhs=items[0])))
		else:
			frags.append(items[0])
	else:
		print items[:2]
		# This is where we need to make our changes
		chosen_expansion = choice(items)
		#print type(chosen_expansion)
		frags.append(generate_sample(grammar, [chosen_expansion]))
	return frags
