#coding=utf-8
from urllib import request,parse
import ssl
import string

ssl._create_default_https_context = ssl._create_unverified_context

class Dumppage():
	def __init__(self,url):
		self.url=url

	def Start_url(self):
		self.url = parse.quote(self.url,safe=string.printable)
		r = request.Request(url=self.url)
		response = request.urlopen(r)
		response = response.read().decode('utf-8')
		return response
