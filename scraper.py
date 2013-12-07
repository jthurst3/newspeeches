# scraper.py
# scrapes a political speech from the specified website
# J. Hassler Thurston
# RocHack Hackathon December 7, 2013

from bs4 import BeautifulSoup
import urllib

# websites supported = http://www.presidentialrhetoric.com/

# list of things to be removed from HTML text
remove_items = ['','print','close window',' ']
# list of things to be removed from HTML text, if text contains these items
remove_parameters = ['<','>','{','}','\t','www.','        this page']
# list of things that must be present in HTML text
must_have_items = ['.']

# gets a list of relevant lines from the transcript of the speech found on the specified webpage
def get_line_list(webpage):
	html = urllib.urlopen(webpage).read() # fetch HTML from webpage
	soup = BeautifulSoup(html)
	text = soup.get_text() # get the text from the HTML page
	split = text.split('\n') # split on newlines
	ascii = convert_list_to_ascii(split)
	for item in remove_items:
		ascii = [x for x in ascii if x != item]
	# from http://stackoverflow.com/questions/2793324/is-there-a-simple-way-to-delete-a-list-element-by-value-in-python
	for param in remove_parameters:
		ascii = [x for x in ascii if (param not in x)]
	politician = ascii[0] # assume the politician's name is the first element in the list (good for current website supported)
	#print politician
	for item in must_have_items:
		ascii = [x for x in ascii if (item in x)]
	return ascii, politician

# converts a list to ASCII format, where any line with unicode characters gets removed
def convert_list_to_ascii(ls):
	ascii = []
	for line in ls:
		newline = ''
		try:
			# from http://stackoverflow.com/questions/2365411/python-convert-unicode-to-ascii-without-errors
			newline = line.encode('ascii')
		except UnicodeEncodeError:
			pass
		ascii.append(newline)
	return ascii




