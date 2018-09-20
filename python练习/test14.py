import re
# phone=input("请输入手机号：")
# print("输入的手机号为：%s"%phone)
# result=re.match("\d{3}",phone)

# str=result.group()
# print("您的网段为：%s"%str)
# 
# email=input("请输入邮箱：")
# print("您的邮箱为：%s"%email)
# result=re.match("([\w]{4,20})@(163\.com)",email)
# str=result.group(2)
# print("您的域名为：%s"%str)

# id=input("请输入身份证号：")
# print("您的身份证号为：%s"%id)
# result=re.match("(\d{3})\d{14}[0-9x]",id)
# str=result.group(1)
# print(str)
# 
# 
# result=re.match(r"<(\w+)><(\w)>(.*)</\2></\1>","<div><p>hellor</p></div>")
# str=result.group(3)
# print(str)
# 
# html='''<div>
# <p>岗位职责：</p>
# <p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>
# <p><br></p>
# <p>必备要求：</p>
# <p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
# <p>&nbsp;<br></p>
# <p>技术要求：</p>
# <p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>
# <p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p>
# <p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<br></p>
# <p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p>
# <p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>
# <p>&nbsp;<br></p>
# <p>加分项：</p>
# <p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>
# </div>'''
# result=re.sub(r"</?\w+>|&nbsp;|\n","",html)
# print(result)
# 
# html="<img src=\"http://www.sina.com.cn/pic/abc.jpeg\"/>"
# result=re.sub(r'<img\ssrc=|/>|"',"",html)
# print(result)
# 
# html="<a href=\"http://www.sina.com.cn\">新浪</a>"
# result=re.sub(r'<a\shref=|</a>|"',"",html)
# result2=re.sub(r'>',"\n",result)
# print(result2)
# 
html=["http://www.interoem.com/messageinfo.asp?id=35"
"http://3995503.com/class/class09/news_show.asp?id=14"
"http://lib.wzmc.edu.cn/news/onews.asp?id=769"
"http://www.zy-ls.com/alfx.asp?newsid=377&id=6"
"http://www.fincm.com/newslist.asp?id=415"]


for fi in html:
	result=re.match(r"http://\w*/",fi)
	
