"""

def print_hello(a,b):
    print("즐거운 월요일입니다"*7)


print(print_hello(a,b))

"""

#변형
def print_hello(a,b):
    mul = a*b
    print(mul)

user_input = input("문장")
user_input2 = int(input("횟수"))

print_hello(user_input, user_input2)
"""
#변형
def print_hello(a,b):
    for i in range(b):
        print(a)

user_input = input("문장")
user_input2 = input("횟수")

print_hello(user_input, user_input2)
"""