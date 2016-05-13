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

	def p(self, string):
		return " ".join(string.split())

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

	def getDate(self, soup):
		dates = soup.find_all("div", class_="normal")
		return dates[1].text.encode("utf-8").strip()

	def getMessages(self, soup):
		messages = soup.find_all("div", class_="voz-post-message")
		mess =""		
		for message in messages:
			mess = mess.strip() + "." + self.p(str(message.text)).encode("utf-8")
		return mess

	def processSoup(self, soup, link):
		if(soup.title.string.lower().find("tư vấn")!=-1 or soup.title.string.lower().find("cấu hình")!=-1):
			date = self.getDate(soup)
			mess = self.getMessages(soup)
			print 'importing data'
			self.writeFile(link+";"+soup.title.string.encode("utf-8")+";"+mess+";"+date+"\n")
		else:
			print 'no data to import'

	def start(self):
		for link in self.crawllist:
			print 'Start to crawl: ' + link 
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
		print 'done!'


