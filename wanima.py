from config import Configs
from dumppage import Dumppage
from parsepage import Parespage
from mongoDBConn import mongo



cf = Configs()
for url in cf.urls:
# 将url给dumppage进行请求
	dp = Dumppage(url)
	html = dp.Start_url()

# 对页面分析
	pg=Parespage(html)

#next_link 存储在next_addr列表中
	# pg.Next_addr1()
	# print(pg.next_addr)



# 图片地址存储在picture_addr列表中
	pg.Picture_addr()
	picturl=pg.picture_addr

