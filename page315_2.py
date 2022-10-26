a_min = 2 # 앉힐 수 있는 최소 사람 수
b_max = 10 # 앉힐 수 있는 최대 사람 수
c_all = 100 # 전체 사람의 수
memo = {}

def q(nam,an): # 문제(남은 사람수, 앉힌 사람수)
    key = str([nam,an]) # 남은 사람수, 앉힌 사람수

    # 종료조건
    if key in memo:
        return memo[key] # 메모화
    if nam < 0: # 남은 사람수
        return 0 # 무효이므로 0을 리턴
    if nam == 0: # 남은 사람수
        return 1 # 유효하므로 수를 세기 위해 1을 리턴
    
    #재귀처리
    count = 0
    for i in range(an, b_max+1): # 앉힌사람수, 앉힐수있는 최대사람수
        count +=  q(nam-i, i)

    #메모화처리
    memo[key] = count
    
    # 종료
    return count

print(q(c_all,a_min))

