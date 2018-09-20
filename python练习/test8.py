def f1():
	print("方法1")
def f2(a,b,c):
	d=a+b-c
	print(d)

student={{"id":1,"name":"tom","age":20},{"id":2,"name":"mary","age":21}}
def f3():
	print("学生管理系统")
	print("1.查看所有学生")
	print("2.添加学生")
	print("3.添加学生")
	print("4.添加学生")
	print("3.退出")
	choice=int(input("请选择："))
	if choice==1:
		showstudent()
	elif(choice==2):
		addstudent()
	elif(choice==3):
		print("退出成功")
def showstudent():
	print("姓名")
	for s in student.keys():
		str=student[s]
		print(str["id"],str["name"],str["age"])
	f3()
def addstudent():
	name=input("请输入学生姓名：")
	student.append(name)
	if len(student)>0:
		print("添加成功")
		f3()
def f4(num):
	if num==1:
		return 1
	if num==2:
		return 1
	return f4(num-1)+f4(num-2)




