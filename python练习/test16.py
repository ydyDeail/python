import requests
from bs4 import BeautifulSoup


baseurl="http://sh.zu.fang.com"
res=requests.get(baseurl)
res.encoding="gb2312"
soup=BeautifulSoup(res.text,'html.parser')
add={}
addressli=soup.select(".search-list dd:nth-of-type(1) a")
for address in addressli:
	addname=address.text
	addurl=address["href"]
	add[addname]=addurl
def addInfo(go,end,addname="不限"):
	for pageNo in range(go,end+1):
		print("开始第%d页"%pageNo)
		if pageNo==1:
			url=baseurl+add[addname]
		else:
			url=baseurl+add[addname]+"i3"+str(pageNo)+"/"
		if addname=="不限":
			url=baseurl
		infourl(url)

def infourl2(zhuurl):
	try:
		res=requests.get(zhuurl)
		res.encoding="gb2312"
		soup=BeautifulSoup(res.text,'html.parser')
		name=soup.select(".clearfix div[class='tab-cont clearfix'] .title")[0].text
		huxing=soup.select(".clearfix div[class='tab-cont clearfix'] .tab-cont-right div[class='tr-line clearfix'] div[class='trl-item1 w182'] .tt")[0].text
		s_s=soup.select(".clearfix div[class='tab-cont clearfix'] .tab-cont-right div[class='tr-line clearfix'] div[class='trl-item1 w132'] .tt")[0].text
		chao=soup.select(".clearfix div[class='tab-cont clearfix'] .tab-cont-right div[class='tr-line clearfix'] div[class='trl-item1 w146'] .tt")[1].text
		money=soup.select(".clearfix div[class='tab-cont clearfix'] .tab-cont-right div[class='tr-line clearfix zf_new_title'] div[class='trl-item sty1'] i")[0].text
		ditie=soup.select(".clearfix div[class='tab-cont clearfix'] .tab-cont-right div[class='tr-line'] div[class='trl-item2 clearfix'] .rcont a")[3].text
		address=soup.select(".clearfix div[class='tab-cont clearfix'] .tab-cont-right div[class='tr-line'] div[class='trl-item2 clearfix'] .rcont a")[4].text
		s=s_s[:-2]
		return name+","+huxing+","+s+","+money+","+chao+","+ditie+","+address
	except:
		return "无详情"

def infourl(url):
	res=requests.get(url)
	res.encoding="gb2312"
	soup=BeautifulSoup(res.text,'html.parser')
	link=soup.select(".houseList dl dd p[class='title'] a")
	for links in link:
		zhu1=links["href"]
		zhu2=links["data_channel"]
		zhuurl=baseurl+zhu1+"?channel="+zhu2
		name=infourl2(zhuurl)
		print(name)
addInfo(1,3,"不限")