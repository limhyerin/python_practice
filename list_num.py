# 리스트의 숫자들의 자릿수를 출력하는 프로그램

numbers = [273,103,5,32,65,9,72,800,99]

for num in numbers:
    if num / 100 >= 1:
        print(num,"는 3 자릿수입니다.")

    elif num / 10 >= 1:
        print(num, "는 2 자릿수입니다.")

    elif num / 1 >= 1:
        print(num, "는 1 자릿수입니다.")
        
    else:
        print("잘못된 입력")
