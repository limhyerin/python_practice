# 나누어 떨어지는 숫자를 출력하는 프로그램

user_input = int(input("정수를 입력해주세요 : "))

if user_input % 2 == 0:
    print(user_input,"은 2로 나누어 떨어지는 숫자입니다")
else:
    print(user_input,"은 2로 나누어 떨어지는 숫자가 아닙니다")

if user_input % 3 == 0:
    print(user_input,"은 3으로 나누어 떨어지는 숫자입니다")
else:
    print(user_input,"은 3으로 나누어 떨어지는 숫자가 아닙니다")

if user_input % 4 == 0:
    print(user_input,"은 4로 나누어 떨어지는 숫자입니다")
else:
    print(user_input,"은 4로 나누어 떨어지는 숫자가 아닙니다")

if user_input % 5 == 0:
    print(user_input,"은 5로 나누어 떨어지는 숫자입니다")
else:
    print(user_input,"은 5로 나누어 떨어지는 숫자가 아닙니다")