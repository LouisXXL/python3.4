a=int(input("你答對了幾題？ "))
score=0;
if((a>=0)and(a<=14)):
	if(a<9):
		score=a*8
	else:
		score=64+(a-8)*6
	print(score)
else:
	print("error")
