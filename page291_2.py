def mul(*value):
    num_sum = 1
    for i in value:
        num_sum *= i
    return num_sum

print(mul(5,7,9,10))