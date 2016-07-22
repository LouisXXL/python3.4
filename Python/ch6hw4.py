for i in range(2,501):
	facSum=1
	for j in range(2,int(i**0.5)+1):
		if(i%j==0):
			if(i/j==j):
				facSum+=j
			else:
				facSum+=j+int(i/j)
	if(facSum==i):
		print(str(i),end='')
print("為完全數")
