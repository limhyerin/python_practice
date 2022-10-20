#  달러를 환율로 변환하는 프로그램
# 155달러, 415달러, 78달러, 179달러, 805달러
# 각각 환율에 맞춰 원화로 바꾼뒤 원화라는 이름으로 리스트 출력

dollar = [155, 415, 78, 179, 805]
w = 1434.18
won = []

for i in dollar:
    a = i *w
    a = float(a)
    won.append(a)
print(won)

