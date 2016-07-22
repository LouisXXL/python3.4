try:
	line=open("/home/yongb/ch1.txt","r")
except:
	print("error")
else:
	print("已經讀入")

print(line.read())
line.close()
