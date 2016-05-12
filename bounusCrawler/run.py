from vtquCrawler import vtquCrawler
if __name__ == '__main__':
	try:
		crawler = vtquCrawler()
		crawler.start()
	except Exception as inst:
		print inst
