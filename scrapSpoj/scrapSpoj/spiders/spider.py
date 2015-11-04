import scrapy
import time
import csv
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request

class SpojSpider(scrapy.Spider) :
	name = "spider"
	allowed_domains = ["spoj.com"]
	start_urls = ['http://www.spoj.com/problems/classical/sort=0,start=%s' %s for s in xrange(0, 3251, 50)]
	def parse(self, response) :
		time.sleep(10)
		platform = "Spoj"
		with open("../Data/scrapSpoj.csv","ab+") as f:
			writer = csv.writer(f)
			headers = ["Name", "Slug", "Submissions", "Accuracy", "QuestionURL", "Platform", "Tags", "LanguagesAllowed", "DateAdded"]
			writer.writerow(headers)
			for sel in response.xpath(".//*[@id='content']/div[2]/div[1]/div[2]/table/tbody/tr") :
				if(len(str(sel.xpath('td[2]/a/text()').extract())) > 2) :
					name = sel.xpath('td[2]/a/text()').extract()[0]
					slug = sel.xpath("td[1]/text()").extract()[0].split('\t')[6].split('\n')[0]
					submissions = sel.xpath('td[4]/a/text()').extract()[0]
					questionURL = "http://www.spoj.com" + str(sel.xpath('td[2]/a/@href').extract()[0])
					name = name.encode('utf8')
					slug = slug.encode('utf8')
					submissions = submissions.encode('utf8')
					questionURL = questionURL.encode('utf8')
					accuracy = ""
					tags = ""
					languagesAllowed = ""
					dateAdded = ""
					questionDetailObject = [name, slug, submissions, accuracy, questionURL, platform, tags, languagesAllowed, dateAdded]
					writer.writerow(questionDetailObject.encode('utf8') if type(questionDetailObject) is unicode else questionDetailObject)	
		f.close()
