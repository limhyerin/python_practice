# 각리스트 안의 있는 값들을 character 딕셔너리 안에 키와 값으로 집어넣고 출력하는 프로그램

key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]
character = {}

for i in range(0,len(key_list)):
    character[key_list[i]] = value_list[i]

print(character)