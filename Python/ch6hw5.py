count=int(input("輸入項數"))
if(count>=1):print(str(0),end='')
if(count>=2):print(str(1),end='')
num_1=0
num_2=1
for i in range(2,count):
	print(str(num_1+num_2),end='')
	tm=num_1
	num_1=num_2
	num_2=tm+num_2

