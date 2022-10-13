# datetime 모듈, 현재 월을 받아 계절을 출력하는 프로그램

import datetime  # 모듈 import

now = datetime.datetime.now()  # now 변수에 넣기
month = now.month  # month 변수에 now.month 넣기

if 3 <= month <= 5:  # 봄
    print("현재는 봄입니다")
if 6 <= month <= 8:  # 여름
    print("현재는 여름입니다")
if 9 <= month <= 11:  # 가을
    print("현재는 가을입니다")
if 12 == month or 1 <= month <=2:  # 겨울
    print("현재는 겨울입니다")
