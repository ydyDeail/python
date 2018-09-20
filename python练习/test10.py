import os

def fileinfo():
	print("1.写入信息")
	print("2.读取信息")
	print("3.退出")
	choice=int(input("请选择:"))
	if choice==1:
		writeFile()
	elif choice==2:
		readFile()
	elif choice==3:
		print("退出成功")
def writeFile():
	file=open("mysql.txt","w")
	ip=input("请输入主机ip：")
	port=input("请输入端口号：")
	sqlname=input("请输入数据库名：")
	username=input("请输入用户名：")
	pwd=input("请输入密码：")
	file.write("ip地址:"+ip+"\n")
	file.write("端口号:"+port+"\n")
	file.write("数据库名称:"+sqlname+"\n")
	file.write("用户名:"+username+"\n")
	file.write("密码:"+pwd+"\n")
	print("写入成功")
	file.close()
	fileinfo()
def readFile():
	file=open("mysql.txt","r")
	ip=file.readline()
	ip=ip[ip.find(":")+1:]
	print(ip)
	port=file.readline()
	port=port[port.find(":")+1:]
	print(port)
	sqlname=file.readline()
	sqlname=sqlname[sqlname.find(":")+1:]
	print(sqlname)
	username=file.readline()
	username=username[username.find(":")+1:]
	print(username)
	pwd=file.readline()
	pwd=pwd[pwd.find(":")+1:]
	print(pwd)
	fileinfo()
	file.close()
fileinfo()