import requests
from bs4 import BeautifulSoup
import pandas
def getInfo(url):
    try:
        res=requests.get(url)
        res.encoding="gb2312"
        soup=BeautifulSoup(res.text,'html.parser')
        info=soup.select("div[class='bmsg job_msg inbox']")[0].text
        return info
    except:
        return "无详情"
    
def fenye(go,end):
    resultList=[]
    for pageNo in range(go,end+1):
        print("开始爬取第%s页"%pageNo)
        res=requests.get("https://search.51job.com/list/020000,000000,0000,00,9,99,java,2,"+str(pageNo)+".html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=")
        res.encoding="gb2312"
        soup=BeautifulSoup(res.text,'html.parser')
        jobli=soup.select(".dw_table div[class='el mk'],.dw_table div[class='el']")
        for job in jobli:
            result={}
            link=job.select("p  a")[0]
            result["jobname"]=link.text.strip()
            url=link["href"]
            result["info"]=getInfo(url)
            result["joboffice"]=job.select("span")[1].text
            result["jobmoney"]=job.select("span")[3].text
            resultList.append(result)
    return resultList

print("开始爬取")
li=fenye(1,3)
df=pandas.DataFrame(li)
df.to_excel("d:/jobs.xlsx")
print("爬取成功")