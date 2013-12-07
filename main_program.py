# main_program.py
# runs the parser and produces sentences that politicians might say
# J. Hassler Thurston
# RocHack Hackathon December 7, 2013

import os

from scraper import *
from get_words import *
from parser import *

# TODO: use os.path.set() instead of just referencing local (Mac OS X) filename

speeches_to_get = ['http://www.presidentialrhetoric.com/speeches/08.22.13.print.html',
'http://www.presidentialrhetoric.com/speeches/01.21.13.print.html',
'http://www.presidentialrhetoric.com/speeches/02.04.13.print.html'
]

csv_files = []

def get_and_export(website):
	lines = get_line_list(website)
	words = get_words(lines[0])
	speech_name = get_speech_name(website)
	# make the relevant politician's folder if it doesn't already exist
	# from http://stackoverflow.com/questions/1274405/how-to-create-new-folder
	folder = 'database/' + str(lines[1]) + '/'
	if not os.path.exists(folder): os.makedirs(folder)
	filename = folder + speech_name + '.csv'
	csv_files.append(filename)
	export_to_csv(words, filename)

# gets the speech name from the website (only supports presidentialrhetoric.com currently)
def get_speech_name(website):
	relevant_string = website.split('/')[-1].split('.print.html')
	return relevant_string[0]

# export functionality
def export_fun():
	for speech in speeches_to_get:
		get_and_export(speech)

# adding words functionality
def add_word_fun():
	get_dictionary()
	for csv_file in csv_files:
		add_words(csv_file)

# main program
def main():
	export_fun()
	add_word_fun()


if __name__ == '__main__':
	main()