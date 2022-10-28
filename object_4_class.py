# 별도 추가
class student():
    def create_student(self, name, korean, math, english, science):
            self.name = name
            self.korean = korean
            self.math = math
            self.english = english
            self.science = science

    students = [
        create_student("윤인성", 87, 98, 88, 95),
        create_student("연하진", 92, 98, 96, 98),
        create_student("구지연", 76, 96, 94, 90),
        create_student("나선주", 98, 92, 96, 92),
        create_student("윤아린", 95, 98, 98, 98),
        create_student("윤명월", 64, 88, 92, 92)
    ]

    def score_sum(self):
        return self.korean + self.math + self.english + self.science

    def score_avg(self):
        avg = self.score_sume() / 4
        return avg

a = student()
print(a.score_sum())
print(a.score_avg())