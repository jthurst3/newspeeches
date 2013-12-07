# scraper.py
# scrapes a political speech from the specified website
# J. Hassler Thurston
# RocHack Hackathon December7, 2013

from BeautifulSoup import BeautifulSoup
import url

def scraper(webpage):
	html = urllib.urlopen(webpage)
	print html

if __name__ == '__main__':
	scraper('http://www.google.com')