list_number = [52,273,32,72,100]

# try except 구문으로 예외를 처리합니다
try:
    # 숫자를 입력받습니다
    number_input = int(input("정수입력>>"))
    # 리스트의 요소를 출력합니다
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
    # (고의적으로 넣은 문제 발생부분)
    예외.발생해주세요() # 일방적으로 오류를 넣음/ Name Error
except ValueError as exception:
    print("함수를 입력해주세요")
    print(type(exception), exception)

except IndexError as exception:
    print("리스트의 인덱스를 벗어났어요")
    print(type(exception), exception)

except NameError as exception:
    print(type(exception), exception)