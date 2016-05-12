from vtqCrawler import vtqCrawler
from pattern.web import crawl
from pattern.web import Crawler, DEPTH, BREADTH
from bs4 import BeautifulSoup
if __name__ == "__main__":
	try:
		crawllist = []
		crawllist.append('https://vozforums.com/forumdisplay.php?f=24')
		for i in range(2, 1472):
			crawllist.append('https://vozforums.com/forumdisplay.php?f=24&order=desc&page='+str(i))
		print 'Start to scan ' + str(len(crawllist)) + " sites..."
		for site in crawllist:
			crawler = vtqCrawler(links=[site], delay=0.3, domains=['vozforums.com'])
			while not crawler.done:
				crawler.crawl(method=DEPTH, cached=False)
	except Exception as inst:
		print inst
