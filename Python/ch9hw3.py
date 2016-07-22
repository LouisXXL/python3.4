import random
poker=[]
suit={1:"黑桃", 2:"紅心", 3:"方塊", 4:"梅花"}
card = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
print(suit,"\n",card,"\n\n")

for i in range(1,5):
	for j in range(0,13):
		poker.append(suit[i]+card[j])

for k in range(5):
	get=random.choice(poker)
	print(get,end="")
	print("\n")
	poker.remove(get)
