from vtqCrawler import vtqCrawler

if __name__ == '__main__':
	try:	
		cpu_links =[]
		ram_links =[]
		motherboard_links =[]
		storage_links =[]
		for i in range(1, 10):
			link = "http://pcpartpicker.com/parts/cpu/fetch/?page="+str(i)+"&mode=list&xslug=&search="
			cpu_links.append(link)
		for i in range(1, 51):
			link = "http://pcpartpicker.com/parts/memory/fetch/?page="+str(i)+"&mode=list&xslug=&search="
			ram_links.append(link)
		for i in range(1, 23):
			link = "http://pcpartpicker.com/parts/motherboard/fetch/?page="+str(i)+"&mode=list&xslug=&search="
			motherboard_links.append(link)
		for i in range(1, 27):
			link = "http://pcpartpicker.com/parts/internal-hard-drive/fetch/?page="+str(i)+"&mode=list&xslug=&search="
			storage_links.append(link)

		cpu_crawler = vtqCrawler(cpu_links, 'cpu')
		ram_crawler = vtqCrawler(ram_links, 'ram')
		motherboard_crawler = vtqCrawler(motherboard_links, 'motherboard')
		storage_crawler = vtqCrawler(storage_links, 'storage')
		#cpu_crawler.crawl()
		#ram_crawler.crawl()
		#motherboard_crawler.crawl()
		storage_crawler.crawl()	
	except Exception as inst:
		print inst
