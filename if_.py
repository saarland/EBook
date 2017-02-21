# -*- coding: utf-8 -*-
#age = 20
#print("your age is",age)
#if age >= 20:
#	print("adult")
#else:
#	print("teenager")
#s = input("birth:")

#将字符串类型转换成int型
#birth = int(s)
#if birth<2000:
#	print("00前")
#else:
#	print("00后")

height = 1.75
weight = 80.5
BMI = weight/(height*height)
if(BMI < 18.5):
	print("过轻,BMI值：",BMI)
elif(BMI >=18.5 and BMI < 25):
	print("正常,BMI值：",BMI)
elif(BMI >=25 and BMI < 28):
	print("过重,BMI值：",BMI)
elif(BMI >=28 and BMI < 32):
	print("肥胖,BMI值：",BMI)
else:
	print("严重肥胖,BMI值：",BMI)