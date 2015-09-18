# urllib.request — Extensible library for opening URLs
# https://docs.python.org/3/library/urllib.request.html#module-urllib.request

# Beautiful Soup is a Python library for pulling data out of HTML and XML files
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start

# import urllib.request to make requests to site that will be scraped
import urllib.request
from bs4 import BeautifulSoup


request_content = urllib.request.urlopen('http://iphoneimei.info/?imei=358685052856032')

soup = BeautifulSoup(request_content, 'html.parser')

def Main():
	for link in soup.find_all('a'):
		print(link.get('href'))
    	

if __name__ == '__main__':
	Main()

print(request_content.read())

