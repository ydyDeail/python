class AgeException(Exception):
	def __init__(self,age):
		self.age=age
class Person:
	def __init__(self,name,age):
		self.name=name
		if age<0:
			raise AgeException(age)
		self.age=age
	def  sayHello(self):
		print("我叫：%s,年龄：%d"%(self.name,self.age))
try:
	p1=Person("tom",-15)
	p1.sayHello()
except AgeException as e:
	print("输入的年龄不合法%s"%(e))

