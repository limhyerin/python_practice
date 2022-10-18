#type(대상) is list / dict
character = {
    "name" : {"기사"},
    "level" : 12,
    "items" : {
        "sword":"불꽃의 검",
        "armor":"풀플레이트"
    },
    "skil":["베기","세게 베기", "아주 세게 베기"] 
}

for key in character:
    if type(character[key]) is dict: # 딕셔너리인지 여부 확인
        for i in character[key]: 
            print(i, ":", character[key][i])
    elif type(character[key]) is list: # 리스트인지 여부 확인
        for j in character[key]:
            print(key, ":", j)
    else:
        print(key, ":", character[key])
