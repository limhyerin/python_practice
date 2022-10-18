# 별 피라미드 찍기

for i in range(1, 15):
    for j in range(15-i):
        print(" ", end="") # end=""
    for k in range(1, i*2, 1): # #
        print("*", end="")
    print("")
