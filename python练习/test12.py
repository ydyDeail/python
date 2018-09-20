class pet:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def show(self):
		print("名字：%s\n年龄：%d"%(self.name,self.age))
class dog(pet):
	def __init__(self,name,age,type):
		super().__init__(name,age)
		self.type=type
	def show(self):
		print("名字：%s\n年龄：%d\n品种：%s"%(self.name,self.age,self.type))

d=dog("张三",15,"拉布拉多")
d.show()
def f1():
	print("f1")