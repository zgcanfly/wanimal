import pymongo
import time
class Mongodbconn(object):
	def __init__(self):
		self.date = time.strftime("%F-%T", time.localtime())
		self.clients = pymongo.MongoClient('106.15.224.237',27017)
		self.dbname="wanima"
		self.db=self.clients[self.dbname]
		self.col1=self.db['detail']
		self.col2=self.db['viurl']
		self.col1.ensure_index('ph_url', unique=True)
		self.col2.ensure_index('title', unique=True)

	def Insertcol1(self,url):
		detail1 = {'时间': self.date, 'nexturl': url}
		self.col1.insert(detail1)
		print(detail1,"已经存入")

	def Insertcol2(self,url):
		detail2 = {'时间': self.date, 'picturl': url }
		self.col1.insert(detail2)
		print(detail2,"已经存入")

	def Selectdb(self):
		for item in self.col1.find(no_cursor_timeout=True).batch_size(5):
			return item['ph_url']