line=input()
num=line.split(" ")

num[0]=int(num[0])
num[1]=int(num[1])
num[2]=int(num[2])
print("你輸入的是\n"+str(num[0]),str(num[1]),str(num[2]))
print("\n")
if(num[0]>num[1] and num[0]>num[2]):
	if(num[1]>num[2]):
		print("由小排到大是")
		print(num[2],num[1],num[0])
	else:
		print("由小排到大是")
		print(num[1],num[2],num[0])
elif(num[1]>num[0] and num[1]>num[2]):
	if(num[0]>num[2]):
		print("由小排到大是")
		print(num[2],num[0],num[1])
	else:
		print("由小排到大是")
		print(num[0],num[2],num[1])
elif(num[2]>num[1] and num[2]>num[0]):
	if(num[1]>num[0]):
		print("由小排到大是")
		print(num[0],num[1],num[2])
	else:
		print("由小排到大是")
		print(num[2],num[0],num[1])
else:
	print("error")
