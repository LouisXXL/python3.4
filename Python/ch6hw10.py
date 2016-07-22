num=int(input())
res=0
while(num>0):
	res=res*10+num%10
	num//=10
print(res)
