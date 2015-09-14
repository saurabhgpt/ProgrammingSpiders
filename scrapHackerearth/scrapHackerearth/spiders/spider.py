import scrapy
from scrapHackerearth.items import ScraphackerearthItem
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class scrapHackerearthSpider(scrapy.Spider) :
	name = "spider"
	allowed_domains = ["hackerearth.com"]
	start_urls = [
		"https://www.hackerearth.com/problems"
	]

	def parse(self, response) :
		browser = webdriver.Firefox()
		browser.get(response.url)
		time.sleep(60)
		result = browser.page_source
		for sel in response.xpath(".//*[@id='row']") :
			f_out=open("/home/lethal/PYTHON/PythonEnv/venv/.git/ProgrammingSpiders/scrapHackerearth/scrapHackerearth/Data/scrapHackerearth.csv","a+")
			item = ScraphackerearthItem()
			item['Platform'] = "Hackerearth"
			if(len(str(sel.xpath('td[2]/a/span/text()').extract())) > 2) :
				name = str(sel.xpath('td[2]/a/span/text()').extract())[3:-2].replace("\\", "")
				item['questionURL'] = "https://www.hackerearth.com" + str(sel.xpath('td[2]/a/@href').extract()[0])
				questionDetailObject = {
					"Name" : name,
					"Slug" : str(sel.xpath('td[2]/a/@href').extract()[0]).split("/")[::-1][1],
					"Submissions" : str(sel.xpath('td[3]/span/text()').extract()[0]),
					# "Accuracy" : str(int(str(sel.xpath('td[4]/a/text()').extract()[0]).split("/")[0])*100/int(str(sel.xpath('td[4]/a/text()').extract()[0]).split("/")[1])),
					"tags" : str(sel.xpath('td[5]/text()').extract()[0]).split("\n")[1],
					"questionURL" : str(item['questionURL']),
					"Platform" : str(item['Platform'])
				}
				f_out.write(str(questionDetailObject))
				f_out.write("\n")
			f_out.close()
		browser.quit()
