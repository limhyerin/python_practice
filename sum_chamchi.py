# 클래스에 함수를 추가하는 방법 : 메서드
class 참치선물세트():
    일반 = 0
    야채 = 0
    고추 = 0

    def 총합(self, 이름):
        합 = self.일반 + self.야채 + self.고추
        return 이름 + str(합)

참01호 = 참치선물세트()
참01호.일반 = 12
참01호.야채 = 3
참01호.고추 = 3

출력값 = 참01호.총합("참치선물세트 01호 내용물:")
print(출력값)
