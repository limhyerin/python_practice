# 재귀함수를 이용한 리스트 평탄화
#완전히 중첩안에 있는 중첩까지 해체해서 1차원 리스트로 만듬

def flatten(example):
    output = []
    for item in example:
        if type(item) == list:
            output += flatten(item)
        else:
            output.append(item)
    return output

example = [[1,2,3],[4,[5,6]],7,[8,9]]
print("원본: ", example)
print("변환: ", flatten(example))


# re 
def flat(data):
    output = []
    for item in data:
        if type(item) == list:
            output += flat(item)
        else:
            output.append(item)
    return output

data = [[1,2,3],[4,[5,6]],7,[8,9]]
print(flat(data))