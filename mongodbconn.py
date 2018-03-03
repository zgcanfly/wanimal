import pymongo
import time
class Mongodbconn(object):
	def __init__(self):
		self.date = time.strftime("%F-%T", time.localtime())
		self.clients = pymongo.MongoClient('106.15.224.237',27017)
		self.dbname="wanima"
		self.db=self.clients[self.dbname]
		self.col1=self.db['nexturl']
		self.col2=self.db['picturl']
		self.col1.ensure_index('nexturl', unique=True)
		self.col2.ensure_index('picturl', unique=True)


	def Insertcol1(self,url):
		detail1 = {'时间': self.date, 'nexturl': url}
		try:
			self.col1.insert(detail1)
			print(detail1,"已经存入")
		except:
			print(detail1,"重复存入")


	def Insertcol2(self,url):
		detail2 = {'时间': self.date, 'picturl': url}
		try:
			self.col2.insert(detail2)
			print(detail2,"已经存入")
		except:
			print(detail2,"重复存入")

