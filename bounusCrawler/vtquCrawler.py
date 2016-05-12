# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup, SoupStrainer
import codecs
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import urllib2
import time
import re

class vtquCrawler():
	
	timewait = 2;
	crawllist = []

	def __init__(self):
		for i in range(1, 1472):
			self.crawllist.append('https://vozforums.com/forumdisplay.php?f=24&order=desc&page='+str(i))

	def writeFile(self, content):
     		fileIO = codecs.open("dataset.csv", "a", encoding="utf-8")
		fileIO.write(content)
		fileIO.close()

	def findLinks(self, response):
		soup = BeautifulSoup(response)
		links = []
		for a in soup.find_all('a', href=True):
			if(str(a['href']).find("showthread")!=-1):
				links.append("https://vozforums.com/"+a['href'])
		return links

	def processSoup(self, soup, link):
		if(soup.title.string.lower().find("tư vấn")!=-1):
			resultSet = soup.body.findAll(text=re.compile('(0?[1-9]|[12][0-9]|3[01])-(0?[1-9]|1[012])-((19|20))'))
			date = "?"
			dates = []
			for result in resultSet:
				dates.append(str(result))
			if(len(resultSet)>2):
				date = dates[1].strip()
			messages = soup.find_all("div", class_="voz-post-message")
			mess =""		
			for message in messages:
				mess = mess.strip() + "." + str(message.text).strip().replace("\n", "").replace("\t", "").encode("utf-8")		
			print 'importing data'
			self.writeFile(link+","+soup.title.string.encode("utf-8")+","+mess+","+date+"\n")

	def start(self):
		for link in self.crawllist:
			response = urllib2.urlopen(link)	
			html = response.read()
			links = self.findLinks(html)
			for a in links:
				time.sleep(self.timewait)
				print 'opening link:' + str(a)
				thread = urllib2.urlopen(a)	
				threadContent = thread.read()
				soup = BeautifulSoup(threadContent)
				self.processSoup(soup, a)


