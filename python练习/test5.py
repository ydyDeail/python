import random
office=[[],[],[]]

teacher=["a","b","c","d","e","f","g","h"]
for t in teacher:
	index=random.randint(0,2)
	office[index].append(t)
	if len(office[index])>=3:
		break
for o in office:
	print(o)