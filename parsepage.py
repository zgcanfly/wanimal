from scrapy.selector import Selector

class Parespage():
	def __init__(self,html):
		self.html=html
		self.next_addr=[]
		self.picture_addr=[]


	def Picture_addr(self):
		selector = Selector(text=self.html)
		divs = selector.xpath('//img/@src').extract()
		for i in divs:
			if 'jpg' in i:
				self.picture_addr.append(i)
	def Next_addr(self):
		selector = Selector(text=self.html)
		divs = selector.xpath('//a//@href').extract()
		for i in divs:
			if 'wanimal1983' in i:
				self.next_addr.append(i)




