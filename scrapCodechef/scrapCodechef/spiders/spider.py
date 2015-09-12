import scrapy
from scrapCodechef.items import ScrapcodechefItem
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

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
		browser = webdriver.Firefox()
		browser.get(response.url)
		time.sleep(30)
		result = browser.page_source
		for sel in response.xpath("//*[@id='primary-content']/div/div/div[2]/table/tbody/tr") :
			# 	continue
			f_out=open("/home/lethal/PYTHON/PythonEnv/venv/.git/scrapCodechef/scrapCodechef/Data/scrapCodechef.csv","a+")
			item = ScrapcodechefItem()
			item['Platform'] = "Codechef"
			if(len(str(sel.xpath('td[1]/div[1]/a/b/text()').extract())) > 2) :
				f_out.write("Name: ")
				f_out.write(str(sel.xpath('td[1]/div[1]/a/b/text()').extract()[0]))
				f_out.write(", ")

				f_out.write("Slug: ")
				f_out.write(str(sel.xpath('td[2]/a/text()').extract()[0]))
				f_out.write(", ")

				f_out.write("Submissions: ")
				f_out.write(str(sel.xpath('td[3]/div/text()').extract()[0]))
				f_out.write(", ")

				f_out.write("Accuracy: ")
				f_out.write(str(sel.xpath('td[4]/a/text()').extract()[0]))
				f_out.write(", ")

				f_out.write("questionURL: ")
				item['questionURL'] = "https://www.codechef.com" + str(sel.xpath('td[1]/div/a/@href').extract()[0])
				request = scrapy.Request(item['questionURL'], callback = self.parseQuestionDetails)
				f_out.write(str(item['questionURL']))
				f_out.write(", ")

				f_out.write("Platform: ")
				f_out.write(str(item['Platform']))
				f_out.write("\n")
			f_out.close()
		browser.quit()

	def parseQuestionDetails(self, item, response) :
		# print "YEYYEY"
		item = response.meta['item']
		item = self.getMoreInfo(item, response)
		return item

	def getMoreInfo(self, item, response) :
		f_out.write("tags: ")
		f_out.write(str(response.xpath("//*[@id='problem-page']/div/div/div[1]/div[@id='node-4574316']/table/tbody/tr[4]/td[2]/a/text()").extract()))
		f_out.write(", ")
		f_out.write("dateAdded: ")
		f_out.write(str(response.xpath("//*[@id='problem-page']/div/div/div[1]/div[@id='node-4574316']/table/tbody/tr[5]/td[2]/text()").extract()))
		f_out.write(", ")
		f_out.write("LanguagesAllowed: ")
		item["LanguagesAllowed"] = f_out.write(str(response.xpath("//*[@id='problem-page']/div/div/div[1]/div[@id='node-4574316']/table/tbody/tr[8]/td[2]/text()").extract()))
		f_out.write("\n")
