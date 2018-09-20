oldFileName=input("请输入需要备份的文件名：")
oldFile=open(oldFileName,"r")
#找到文件的点的位置
index=oldFileName.rfind(".")
#创建一个新的文件名
newFileName=oldFileName[:index]+"副本"+oldFileName[index:]
#打开新文件，读取旧文件内的内容写入新文件
newFile=open(newFileName,"w")
for x in oldFile.readlines():
	newFile.write(x)

newFile.close()
oldFile.close()
print("备份成功")