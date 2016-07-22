try:
	import time
	line=open("letter.txt","w")
	recipient=input("請輸入收件人")
	sender=input("請輸入寄件人")
	line.write("Dear"+recipient+"\n\n")
	line.write("\t好久不見\n\n")
	line.write(time.strftime("\t\t\t%Y-%m-%d\n",time.localtime(time.time())))
	line.write("\t\t\t"+sender)
except:
	print("error")
line.close()

#寫入一個txt檔並打入訊息
