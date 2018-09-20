#conding=utf-8
print("请输入语文成绩：")
chinese=float(input())

print("请输入数学成绩：")
math=float(input())

print("请输入英语成绩：")
english=float(input())

print("请输入年龄：")
age=int(input())

go=""
if age>=18:
	go="成年了，考试后网吧见"
else:
	go="小屁孩，网吧是不可能进去的"
print("我的各科成绩分别为\n语文：%f\n数学：%f\n英语：%f\n平均成绩为：%f\n年龄为：%d\n%s"%(chinese,math,english,(chinese+math+english)/3,age,go))