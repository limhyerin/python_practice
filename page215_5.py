"""
실행결과
i = 0, j = 1
i = 0, j = 1
i = 0, j = 1
i = 0, j = 1
[1, 4, 3, 16, 5, 36, 7, 64, 9]
"""

numbers = [1,2,3,4,5,6,7,8,9]

for i in range(0, len(numbers)//2):
    j = (i*2)+1
    print(f"i = {i}, j= {j}")
    numbers[j] = numbers[j]**2

print(numbers)