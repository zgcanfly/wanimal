from config import Configs
from dumppage import Dumppage
from parsepage import Parespage



cf = Configs()
for url in cf.urls:
	dp = Dumppage(url)
	html = dp.Start_url()
	pp=Parespage(html)
	pp.Next_addr()
	for url in pp.next_addr:
		print(url, "\n")
		dp = Dumppage(url)
		html=dp.Start_url()
		pp=Parespage(html)
		pp.Picture_addr()




	# pp.Picture_addr()
	# print(pp.next_addr)


# pp.Picture_addr()
	# picturl=pp.picture_addr

