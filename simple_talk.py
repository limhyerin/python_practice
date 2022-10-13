# 간단한 대화 프로그램
import datetime
now = datetime.datetime.now()

year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute

user_input = input("입력: ")
if user_input == "안녕" or user_input == "안녕하세요":
    print("안녕하세요")

elif user_input == "지금 몇시야?" or user_input == "지금 몇시에요?":
    print("현재 시각은 {}시 {}분입니다".format(hour,minute))

elif user_input == "오늘 날짜" or user_input == "오늘날짜":
    print("{}년 {}월 {}일 입니다".format(year,month,day))

else:
    print(user_input)