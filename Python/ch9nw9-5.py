try:
	fo=open("/home/yongb/Python/ch8hw2.py","r")
	for line in fo.readlines():
		line=line.strip()
		print(line)
#except:
#	print("error!")
except IndentationError:
	print("縮排錯誤")
except SyntaxWarning:
	print("可疑的語法")
except SyntaxError:
	print("Python3 語法錯誤")
else:
	print("\t")
	print("OK")
print(fo.read())
fo.close()
