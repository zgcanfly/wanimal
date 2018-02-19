from scrapy.selector import Selector

class Parespage():
	def __init__(self,html):
		self.html=html
		self.next_addr=[]
		self.picture_addr=[]


	def Picture_addr(self):
#选择器对页面进行解析取出img
		selector = Selector(text=self.html)
		divs = selector.xpath('//img/@src').extract()

#对解析出的img进行删选jpg files
		for i in divs:
			if 'jpg' in i:
				self.picture_addr.append(i)


	def Next_addr1(self):

#选择器对页面进行解析取出next_link
		selector = Selector(text=self.html)
		divs = selector.xpath('//a//@href').extract()
		for i in divs:
			if 'wanimal1983' in i:
				self.next_addr.append(i)
	def Next_addr2(self):
		i = 0
		while True:
			i +=1
			j=i
			'http: // wanimal1983.org/page/' + str(j)



