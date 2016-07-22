first=int(input("第一個數字"))
second=int(input("第二個數字"))
while(first>0 and second>0):
	if(first>second):
		first=first%second
	else:
		second=second%first
if(first==0):
	print("最大公因數"+str(second))

else:
	print("最大公因數"+str(first))


