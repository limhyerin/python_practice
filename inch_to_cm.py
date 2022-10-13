# inch 단위를 cm 단위로 변경하는 프로그램
# 1 inch = 2.54 cm

inch_input = input("확인하려는 inch를 입력하세요 ")
float_input = float(inch_input)
cm = float_input * 2.54

print(inch_input, "inch는 ", cm, "cm입니다.")