# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup, SoupStrainer
import codecs
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import urllib2
import time
import re
import json

class vtqCrawler():
	
	timewait = 2;
	crawllist = []
	item = ""

	def __init__(self, links, item ):
		self.crawllist = links
		self.item = item

	def p(self, code):
		return ' '.join(code.split())

	def extrac_spec(self, start_index, end_index, s):
		spec = ""
		for i  in range(start_index + 1, end_index):
			spec = spec + " " + s[i]
		return spec
 
	def writeFile(self, content):
     		fileIO = codecs.open(self.item + ".csv", "a", encoding="utf-8")
		fileIO.write(content)
		fileIO.close()

	def findLinks(self, data):
		parsed_json = json.loads(data)
		found_links = []
		for cpuid in parsed_json['result']['data']:
			found_links.append("http://pcpartpicker.com/part/"+parsed_json['result']['data'][cpuid]['slug'])
		return found_links

	def getSpecs(self, soup):
		specs_block = soup.find_all("div", class_="specs block")
		specs = soup.title.string.replace(" - PCPartPicker","")
		rate = str(soup.find("span", {"itemprop":"ratingValue"}).text)
		num_rate = str(soup.find("span", {"itemprop":"ratingCount"}).text)
		if(self.item == 'ram'):
			for block in specs_block:
				a = self.p(block.text).split(" ")
				specs = specs.strip() + "," + self.extrac_spec(a.index('Manufacturer'), a.index('Part'), a) + "," + self.extrac_spec(a.index('#'), a.index('Type'), a) + "," + self.extrac_spec(a.index('Type'), a.index('Speed'), a) + "," + self.extrac_spec(a.index('Speed'), a.index('Size'), a) + "," + self.extrac_spec(a.index('Size'), a.index('CAS'), a) + "," + self.extrac_spec(a.index('Latency'), a.index('Voltage'), a) + "," + self.extrac_spec(a.index('Voltage'), a.index('Heat'), a) + "," + self.extrac_spec(a.index('Spreader'), a.index('ECC'), a) + "," + self.extrac_spec(a.index('ECC'), a.index('Registered'), a) + "," + self.extrac_spec(a.index('Registered'), a.index('Color'), a)+ "," +self.extrac_spec(a.index('Color'), len(a), a) + "," +rate + "," + num_rate
		elif(self.item == 'cpu'):
			for block in specs_block:
				a = self.p(block.text).split(" ")
				specs = specs.strip() + "," + self.extrac_spec(a.index('Manufacturer'), a.index('Model'), a) + "," + self.extrac_spec(a.index('Model'), a.index('Part'), a) + "," + self.extrac_spec(a.index('#'), a.index('Data'), a) + "," + self.extrac_spec(a.index('Width'), a.index('Socket'), a) + "," + self.extrac_spec(a.index('Socket'), a.index('Operating'), a) + "," + self.extrac_spec(a.index('Frequency'), a.index('Cores'), a) + "," + self.extrac_spec(a.index('Cores'), a.index('L1'), a) + "," + self.extrac_spec(a.index('Cache'), a.index('L2'), a) + "," + self.extrac_spec(a.index('L2') + 1, a.index('L3'), a) + "," + self.extrac_spec(a.index('L3') + 1, a.index('Lithography'), a) + "," + self.extrac_spec(a.index('Lithography'), a.index('Thermal'), a) + "," + self.extrac_spec(a.index('Power'), a.index('Includes'), a) + "," + self.extrac_spec(a.index('Cooler'), a.index('Hyper-Threading'), a) + "," + self.extrac_spec(a.index('Hyper-Threading'), a.index('Integrated'), a) + "," + self.extrac_spec(a.index('Graphics'), len(a), a) + "," +rate + "," + num_rate

		elif(self.item == 'motherboard'):
			for block in specs_block:
				a = self.p(block.text).split(" ")
				specs = specs.strip() + "," + self.extrac_spec(a.index('Manufacturer'), a.index('Part'), a) + "," + self.extrac_spec(a.index('#'), a.index('Form'), a) + "," + self.extrac_spec(a.index('Factor'), a.index('CPU'), a) + "," + self.extrac_spec(a.index('Socket'), a.index('Chipset'), a) + "," + self.extrac_spec(a.index('Chipset'), a.index('Memory'), a) + "," + self.extrac_spec(a.index('Slots'), a.index('Type')-1, a) + "," + self.extrac_spec(a.index('Type'), a.index('Maximum'), a) + "," + self.extrac_spec(a.index('Supported')+1, a.index('RAID'), a) + "," + self.extrac_spec(a.index('Support'), a.index('Onboard'), a) + "," + self.extrac_spec(a.index('Video'), a.index('CrossFire'), a) + "," + self.extrac_spec(a.index('CrossFire')+1, a.index('SLI'), a) + "," + self.extrac_spec(a.index('SLI')+1, a.index('Ethernet')-1, a) + "," + self.extrac_spec(a.index('Ethernet'), a.index('USB')-1, a) + "," + self.extrac_spec(a.index('Header(s)'), len(a), a) + "," +rate + "," + num_rate

		elif(self.item == 'storage'):
			for block in specs_block:
				a = self.p(block.text).split(" ")
				specs = specs.strip() + "," + self.extrac_spec(a.index('Manufacturer'), a.index('Part'), a) + "," + self.extrac_spec(a.index('#'), a.index('Capacity'), a) + "," + self.extrac_spec(a.index('Capacity'), a.index('Interface'), a) + "," + self.extrac_spec(a.index('Interface'), a.index('Cache'), a) + "," + self.extrac_spec(a.index('Cache'), a.index('Form'), a) + "," + self.extrac_spec(a.index('Factor'), a.index('Price/GB'), a) +","+ self.extrac_spec(a.index('Price/GB'), len(a), a) + "," +rate + "," + num_rate
		return specs

	def processSoup(self, soup, link):
		specs = self.getSpecs(soup)
		print 'importing data'
		#mess = specs.title.string
		self.writeFile(specs+"\n")

	def crawl(self):
		for link in self.crawllist:
			print 'Start to crawl: ' + link 
			response = urllib2.urlopen(link)	
			data = response.read()
			links = self.findLinks(data)
			for a in links:
				time.sleep(self.timewait)
				print 'opening link:' + str(a)
				part = urllib2.urlopen(a)	
				partContent = part.read()
				#print partContent
				soup = BeautifulSoup(partContent)
				self.processSoup(soup, a)
		print 'done!'


