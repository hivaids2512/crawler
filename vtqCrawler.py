# -*- coding: utf-8 -*-
from pattern.web import Crawler, DEPTH, BREADTH
from bs4 import BeautifulSoup
import re
import codecs
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
class vtqCrawler(Crawler):

     def writeFile(self, content):
     	fileIO = codecs.open("dataset.csv", "a", encoding="utf-8")
	fileIO.write(content)
	fileIO.close()

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
		self.writeFile(link.url+","+soup.title.string.encode("utf-8")+","+mess+","+date+"\n")

     def priority(self, link, method=DEPTH):
        if "?" in link.url:
            # This ignores links with a querystring.
            return 0.0
        else:
            # Otherwise use the default priority ranker,
            # i.e. the priority depends on DEPTH or BREADTH crawl mode.
            return Crawler.priority(self, link, method)	

     def visit(self, link, source=None):
	crawllist = []
	crawllist.append('https://vozforums.com/forumdisplay.php?f=24')
	for i in range(2, 1472):
		crawllist.append('https://vozforums.com/forumdisplay.php?f=24&order=desc&page='+str(i))
	if(link.referrer in crawllist):	
		if(link.url.find("showthread")!=-1):
			print 'visited:', repr(link.url), 
			print 'from:', link.referrer
			soup = BeautifulSoup(str(source))
			print soup.title.string.strip()
			self.processSoup(soup, link)
		
     def fail(self, link):
	#if(link.url.find("threads")!=-1):
        print 'failed:', repr(link.url), 'from:', link.referrer
