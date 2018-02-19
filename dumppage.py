from urllib import request
import ssl
#防止https错误
ssl._create_default_https_context = ssl._create_unverified_context

class Dumppage():
	def __init__(self,url):
		self.url=url

#request 页面
	def Start_url(self):
		r = request.Request(url=self.url)
		response = request.urlopen(r)
		response = response.read().decode('utf-8')

#返回请求的页面数据
		return response

