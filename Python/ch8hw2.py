def freedom(k):
	for i in range(1,k+1):
		for j in range(1,k+1):
			print(i*j,end="\t")
		print("\n")
	print('\t')

for i in range(1,10):
	freedom(i)
	

