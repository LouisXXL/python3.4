Year = input("請輸入西元年份：")

if ( int(Year) % 400 == 0) :
	print("閏年")
elif( int(Year) % 100 == 0) :	
	print("平年")
elif ( int(Year) % 4 == 0) :
	print("閏年")	
else :
	print("平年")
