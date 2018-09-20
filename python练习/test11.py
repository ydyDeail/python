import pymysql
def menu():
	print("学生管理系统")
	print("1.添加学生")
	print("2.查看学生")
	print("3.修改学生")
	print("4.删除学生")
	print("5.退出")
	choice=int(input("请选择："))
	if choice==1:
		addstudent()
	elif choice==2:
		showstudent()
	elif choice==3:
		updatestudent()
	elif choice==4:
		showstudent()
	elif choice==5:
		print("谢谢使用")	

def addstudent():
	db=pymysql.connect(host="localhost",user="root",
	password="root",db="user",port=3306,charset="utf8")
	name=input("请输入学生姓名：")
	age=int(input("请输入学生年龄："))
	sql='''insert into 
		users(name,age) 
		values('%s',%d)'''%(name,age)
	c=db.cursor()
	c.execute(sql)
	db.commit()
	db.close()
	print("添加成功")
	menu()

def showstudent():
	db=pymysql.connect(host="localhost",user="root",
	password="root",db="user",port=3306,charset="utf8")
	sql='''select id,name,age from users'''
	c=db.cursor()
	c.execute(sql)
	result=c.fetchall()
	print("学号\t姓名\t年龄")
	for row in result:
		print("%d\t%s\t%d"%(row[0],row[1],row[2]))
	db.close()
	menu()

def updatestudent():
	db=pymysql.connect(host="localhost",user="root",
	password="root",db="user",port=3306,charset="utf8")
	stuId=int(input("请输入学生ID："))
	name=input("请输入学生姓名：")
	age=int(input("请输入学生年龄："))
	sql='''update user set name=%s,age=%d where id=%d'''%(name,age,stuId)
	c=db.cursor()
	c.execute(sql)
	db.commit()
	db.close()
	print("修改成功")
	menu()

def deletestudent():
	db=pymysql.connect(host="localhost",user="root",
	password="root",db="user",port=3306,charset="utf8")
	stuId=int(input("请输入学生ID："))
	sql='''delete from user where id=%d'''%(stuId)
	c=db.cursor()
	c.execute(sql)
	db.commit()
	db.close()
	print("删除成功")
	menu()

menu()