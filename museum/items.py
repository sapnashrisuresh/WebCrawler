# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class Website(Item):
	imageurl = Field()
	artistname = Field()
	biographicaldata = Field()
	title = Field()
	date = Field()
	medium =Field()
	dimensions = Field()
	creditline = Field()
	accession = Field()
	copyright = Field()
	artworktype = Field()
	link = Field()