# 염기서열을 입력받아 3글자씩 추출해서 개수를 출력하는 프로그램

user_input = input("염기 서열을 입력해주세요 : ")
counter = {}

for i in range(0, len(user_input),3):
    codon = user_input[i:i+3]

    if len(codon)==3:
        if codon not in counter:
            counter[codon] = 0
        counter[codon]+=1
    
    # len(codon)의 길이가 3이 아닐경우는 따로 안함
print(counter)

