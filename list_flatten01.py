
def flatten(data):
    output = []
    for item in data:
        if type(item) == list:
            output += item
        else:
            output.append(item)
    return output

example = [[1,2,3],[4,[5,6]],7,[8,9]]
print("원본: ", example)
print("변환: ", flatten(example))

"""
def flatten(example):
    output = []
    for i in example:
        if type(i) == list:
            for j in i:
                output.append(j)
        else:
            output.append(i)
    return output

example = [[1,2,3],[4,[5,6]],7,[8,9]]
print(flatten(example))

"""