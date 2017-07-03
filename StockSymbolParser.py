from bs4 import BeautifulSoup
import urllib.request

def all_symbols():
	all_symbols = []
	for i in range(ord('A'), ord('Z') + 1):
		start_letter = chr(i)
		url = 'http://eoddata.com/stocklist/NASDAQ/' + start_letter + '.htm'
		r = urllib.request.urlopen(url).read()
		soup = BeautifulSoup(r, "lxml")
		all_symbols += find_symbols(soup)
	f = open('StockTickers', 'w')
	for i in all_symbols:
		f.write(i + "\n")

def find_symbols(soup):
	rv = []
	a = soup.find_all('td')
	for i in range(len(a)):
		a[i] = str(a[i])
	a = list(filter(lambda i: True if "<td><a href=\"/stockquote/NASDAQ/" in i else False, a))
	a = list(map(lambda i: i[:-9], a))
	for i in a:
		symbol, j = "", -1
		while i[j].isalpha():
			symbol = i[j] + symbol
			j -= 1
		rv += [symbol]
	return rv

all_symbols()