num=int(input("請輸入一個正整數"))
factorialSum=0
for i in range(num):
	factorial=1
	for j in range(i+1):
		factorial*=(j+1)
	factorialSum+=factorial
print(factorialSum)
