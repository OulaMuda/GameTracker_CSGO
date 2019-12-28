from bs4 import BeautifulSoup
import requests
import csv
#import codecs
#import sys
#import io

#file = open('test.html','rb')
#content = file.read().decode('utf-8')

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') 
def getPages(page, writer):
	url = 'https://www.gametracker.com/search/csgo/?searchipp=50&searchpge='+str(page) +'#search'
	response = requests.get(url)
	s = response.content
	content = s.decode('utf-8')
	soup = BeautifulSoup(content,"html5lib")
	tbody = soup.find('table', class_='table_lst table_lst_srs').tbody
	if(tbody != None):
		trindex=0
		for tr in tbody:
			if((trindex != 0) and (trindex != 1) and (trindex != 102) and (trindex != 103) and (trindex % 2 != 1)):
				tds = tr.find_all('td')
				writer.writerow([tds[2].a.text.strip(), tds[3].text.strip(), tds[7].text.strip()])
			trindex+=1


with open('some.csv', 'w', newline ='', encoding = 'gb18030') as csvfile:
	writer = csv.writer(csvfile)
	for idx in range(1,1087):
		print('get page'+str(idx))
		getPages(idx, writer)