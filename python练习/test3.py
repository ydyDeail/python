import random
a=random.randint(1,3)

print("请选择 1.剪刀  2.石头  3.布:")
choice=int(input())
if (choice==1) and (a==2):
	print("玩家输!")
elif (choice==1) and (a==3):
	print("玩家赢!")
elif (choice==2) and (a==1):
	print("玩家赢!")
elif (choice==2) and (a==3):
	print("玩家输!")
elif (choice==3) and (a==1):
	print("玩家输!")
elif (choice==3) and (a==2):
	print("玩家赢!")
elif choice==a:
	print("平局!")
else:
	print("输入不在提示内!")