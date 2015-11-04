import scrapy
from codeforces.items import CodeforcesItem
import time
import csv
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request

class CodeforcesSpider(scrapy.Spider) :
	name = "spider"
	allowed_domains = ["codeforces.com"]
	start_urls = ['http://codeforces.com/problemset/page/%s' %s for s in xrange(1,27)]
	i = 3
	def parse(self, response) :
		time.sleep(10)
		platform = "Codeforces"
		with open("../Data/scrapCodeforces.csv","ab+") as f:
			writer = csv.writer(f)
			headers = ["Name", "Slug", "Submissions", "Accuracy", "QuestionURL", "Platform", "Tags", "LanguagesAllowed", "DateAdded"]
			writer.writerow(headers)
			for sel in response.xpath('//*[@id="pageContent"]/div[2]/div[6]/table/tr') :
				if(len(str(sel.xpath('td[2]/div[1]/a/text()').extract())) > 2) :
					name = sel.xpath('td[2]/div[1]/a/text()').extract()[0].split('\n')[1]
					slug = sel.xpath("td[1]/a/text()").extract()[0].split('\n')[1].split('\r')[0]
					submissions = sel.xpath('td[4]/a/text()').extract()[0].split('x')[-1]
					lis = sel.xpath('td[2]/div[2]/a/text()').extract()
					tags = []
					for i in lis :
						tags.append(str(i).encode('utf8'))		
					questionURL = "https://www.codeforces.com" + str(sel.xpath('td[2]/div[1]/a/@href').extract()[0])
					name = name.encode('utf8')
					slug = slug.encode('utf8')
					submissions = submissions.encode('utf8')
					questionURL = questionURL.encode('utf8')
					accuracy = ""
					languagesAllowed = ""
					dateAdded = ""
					questionDetailObject = [name, slug, submissions, accuracy, questionURL, platform, tags, languagesAllowed, dateAdded]
					writer.writerow(questionDetailObject.encode('utf8') if type(questionDetailObject) is unicode else questionDetailObject)	
		f.close()
