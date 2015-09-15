import scrapy
from scrapHackerearth.items import ScraphackerearthItem
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

class scrapHackerearthSpider(scrapy.Spider) :
	name = "spider"
	allowed_domains = ["hackerearth.com"]
	start_urls = [
		"https://www.hackerearth.com/problems"
	]

	def parse(self, response) :
		browser = webdriver.Firefox()
		browser.get(response.url)
		time.sleep(30)
		platform = "Hackerearth"
		with open("/home/lethal/PYTHON/PythonEnv/venv/.git/ProgrammingSpiders/scrapHackerearth/scrapHackerearth/Data/scrapHackerearth.csv","ab+") as f:
			writer = csv.writer(f)
			headers = ["Name", "Slug", "Submissions", "Tags", "QuestionURL", "Platform"]
			writer.writerow(headers)
			for sel in response.xpath(".//*[@id='row']") :
				if(len(str(sel.xpath('td[2]/a/span/text()').extract())) > 2) :
					name = sel.xpath('td[2]/a/span/text()').extract()[0]
					slug = str(sel.xpath('td[2]/a/@href').extract()[0]).split("/")[::-1][1]
					submissions = sel.xpath('td[3]/span/text()').extract()[0]
					tags = str(sel.xpath('td[5]/text()').extract()[0]).split("\n")[1]
					questionURL = "https://www.hackerearth.com" + str(sel.xpath('td[2]/a/@href').extract()[0])
					name = name.encode('utf8')
					slug = slug.encode('utf8')
					submissions = submissions.encode('utf8')
					tags = tags.encode('utf8')
					questionURL = questionURL.encode('utf8')
					questionDetailObject = [name, slug, submissions, tags, questionURL, platform]
					writer.writerow(questionDetailObject.encode('utf8') if type(questionDetailObject) is unicode else questionDetailObject)
		f.close()
		browser.quit()