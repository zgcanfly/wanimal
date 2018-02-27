from scrapy.selector import Selector
from mongodbconn import Mongodbconn


class Parespage():
	def __init__(self,html):
		self.html=html
		self.next_addr=[]
		self.picture_addr=[]


	def Picture_addr(self):
		print("\n正在解析！")
		selector = Selector(text=self.html)
		divs = selector.xpath('//img/@src').extract()
		for url in divs:
			if 'jpg' in url:
				self.picture_addr.append(url)
				mg = Mongodbconn()
				mg.Insertcol2(url)
	def Next_addr(self):
		print("\n正在解析！")
		selector = Selector(text=self.html)
		divs = selector.xpath('//a//@href').extract()
		for url in divs:
			if 'wanimal1983' in url:
				self.next_addr.append(url)
				mg = Mongodbconn()
				mg.Insertcol1(url)





