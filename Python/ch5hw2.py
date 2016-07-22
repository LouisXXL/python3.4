Height = int(input("請輸入身高(公分)："))
Weight = int(input("請輸入體重(公斤)："))
BMI = float(Weight) / (float(Height)/100)**2

if (BMI < 18.5):
	print("BMI值為%.2f\n，屬體重過輕" % BMI)
elif (18.6 <= BMI and BMI < 24):
	print("BMI值為%.2f\n，屬正常範圍" % BMI)
elif (24 <= BMI and BMI < 27):
	print("BMI值為%.2f\n，屬稍重" % BMI)
elif (27 <= BMI and BMI < 30):
	print("BMI值為%.2f\n,屬輕度肥胖" % BMI)
elif (30 <= BMI and BMI < 35):	
	print("BMI值為%.2f\n，屬中度肥胖" % BMI)
else:
	print("BMI值為%.2f\n，屬重度肥胖" % BMI)
