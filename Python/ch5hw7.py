num_str=input("請輸入3個數字，並以半型空白作為區隔")
num=num_str.split()
num.sort()
#排序

num[0]=int(num[0])
num[1]=int(num[1])
num[2]=int(num[2])
#轉換類型

if(num[0]+num[1]>num[2]):
	if(num[0]**2+num[1]**2==num[2]**2):
		print("Ring Triangle")
	else:
		print("Non-Right Triangles")
else:
	print("False")
