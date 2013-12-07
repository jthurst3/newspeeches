# main_program.py
# runs the parser and produces sentences that politicians might say
# J. Hassler Thurston
# RocHack Hackathon December 7, 2013

import os

from scraper import *
from get_words import *

# TODO: use os.path.set() instead of just referencing local (Mac OS X) filename

speeches_to_get = ['http://www.presidentialrhetoric.com/speeches/08.22.13.print.html',
'http://www.presidentialrhetoric.com/speeches/01.21.13.print.html',
'http://www.presidentialrhetoric.com/speeches/02.04.13.print.html'
]

def get_and_export(website):
	lines = get_line_list(website)
	words = get_words(lines[0])
	speech_name = get_speech_name(website)
	# make the relevant politician's folder if it doesn't already exist
	# from http://stackoverflow.com/questions/1274405/how-to-create-new-folder
	folder = 'database/' + str(lines[1]) + '/'
	if not os.path.exists(folder): os.makedirs(folder)
	export_to_csv(words, folder + speech_name + '.csv')

# gets the speech name from the website (only supports presidentialrhetoric.com currently)
def get_speech_name(website):
	relevant_string = website.split('/')[-1].split('.print.html')
	return relevant_string[0]

# main program
def main():
	for speech in speeches_to_get:
		get_and_export(speech)
	# export_to_csv([[1,2,3],[2,2,3],[3,2,3]],'database/obama1.csv')


if __name__ == '__main__':
	main()