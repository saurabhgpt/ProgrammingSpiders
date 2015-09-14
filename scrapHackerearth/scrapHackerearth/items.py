# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class ScraphackerearthItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	Name = Field()
	Slug = Field()
	Submissions = Field()
	Accuracy = Field()
	questionURL = Field()
	Platform = Field()

	tags = Field()
	contestName = Field()
	dateAdded = Field()
	LanguagesAllowed = Field()