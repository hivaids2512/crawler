from pattern.web import Crawler, DEPTH, BREADTH
from bs4 import BeautifulSoup
import codecs
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
class vtqCrawler(Crawler): 

     def visit(self, link, source=None):
	fileIO = codecs.open("dataset.csv", "a", encoding="utf-8")
	if(link.url.find("showthread")!=-1):
		print 'visited:', repr(link.url), 'from:', link.referrer
		soup = BeautifulSoup(source, 'html.parser')	
		print soup.title
		fileIO.write(link.url+","+link.referrer+","+soup.title.encode("utf-8")+"\n")
	fileIO.close()
     def fail(self, link):
	#if(link.url.find("threads")!=-1):
        print 'failed:', repr(link.url), 'from:', link.referrer