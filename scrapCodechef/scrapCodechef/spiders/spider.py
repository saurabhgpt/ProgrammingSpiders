import scrapy
from scrapCodechef.items import ScrapcodechefItem
import time
import csv

class scrapCodechefSpider(scrapy.Spider) :
	name = "spider"
	allowed_domains = ["codechef.com"]
	start_urls = [
		"https://www.codechef.com/problems/school",
		"https://www.codechef.com/problems/easy",
		"https://www.codechef.com/problems/medium",
		"https://www.codechef.com/problems/hard",
		"https://www.codechef.com/problems/challenge",
		"https://www.codechef.com/problems/extcontest"
	]


	def parse(self, response) :
		time.sleep(15)
		platform = "Codechef"
		with open("../Data/scrapCodechef.csv","ab+") as f:
			writer = csv.writer(f)
			headers = ["Name", "Slug", "Submissions", "Accuracy", "QuestionURL", "Platform", "Tags", "LanguagesAllowed", "DateAdded"]
			writer.writerow(headers)
			for sel in response.xpath("//*[@id='primary-content']/div/div/div[2]/table/tbody/tr") :
				if(len(str(sel.xpath('td[1]/div[1]/a/b/text()').extract())) > 2) :
					name = sel.xpath('td[1]/div[1]/a/b/text()').extract()[0]
					slug = sel.xpath('td[2]/a/text()').extract()[0]
					submissions = sel.xpath('td[3]/div/text()').extract()[0]
					accuracy = sel.xpath('td[4]/a/text()').extract()[0]
					questionURL = "https://www.codechef.com" + str(sel.xpath('td[1]/div/a/@href').extract()[0])
					name = name.encode('utf8')
					slug = slug.encode('utf8')
					submissions = submissions.encode('utf8')
					accuracy = accuracy.encode('utf8')
					questionURL = questionURL.encode('utf8')
					tags = ""
					languagesAllowed = ""
					dateAdded = ""
					questionDetailObject = [name, slug, submissions, accuracy, questionURL, platform, tags, languagesAllowed, dateAdded]
					writer.writerow(questionDetailObject.encode('utf8') if type(questionDetailObject) is unicode else questionDetailObject)
		f.close()
