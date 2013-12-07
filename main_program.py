# main_program.py
# runs the parser and produces sentences that politicians might say
# J. Hassler Thurston
# RocHack Hackathon December 7, 2013

from scraper import *
from get_words import *

def main():
	lines = get_line_list('http://www.presidentialrhetoric.com/speeches/08.28.13.print.html')
	words = get_words(lines)
	print words


if __name__ == '__main__':
	main()