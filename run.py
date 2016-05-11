from vtqCrawler import vtqCrawler
from pattern.web import crawl
from pattern.web import Crawler, DEPTH, BREADTH
from bs4 import BeautifulSoup
if __name__ == "__main__":
	try:
		#fileIO = open("dataset.csv", "wb")
		crawler = vtqCrawler(links=['https://vozforums.com/forumdisplay.php?f=24'], delay=0.0, domains=['vozforums.com'])
		while not crawler.done:
			crawler.crawl(method=DEPTH, cached=False)
	except Exception as inst:
		print inst
