from config import Configs
from dumppage import Dumppage
from parsepage import Parespage



cf = Configs()
for url in cf.urls:
	dp = Dumppage(url)
	html = dp.Start_url()

	pp=Parespage(html)

	pp.Next_addr()
	print(pp.next_addr)


# pp.Picture_addr()
	# picturl=pp.picture_addr

