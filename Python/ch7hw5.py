row1=input("請輸入矩陣第1列")
row2=input("請輸入矩陣第2")


#分割
row1=row1.split()
row2=row2.split()

matrix=[row1,row2]

print("你輸入的是",matrix)
for m in range(3):
	for n in range(2):
		print(matrix[n][m],end=" ")
	print()
