numbers = [273,103,5,32,65,9,72,800,90]

for num in numbers:
    if num / 100 >= 1:
        print(num, "는", len(str(num)),"자릿수입니다") #len(str(num)) 사용해서 자릿수 변경
    elif num / 10 >= 1:
        print(num, "는", len(str(num)),"자릿수입니다") #len(str(num)) 사용해서 자릿수 변경
    elif num/ 1 >= 1:
        print(num, "는", len(str(num)),"자릿수입니다") #len(str(num)) 사용해서 자릿수 변경