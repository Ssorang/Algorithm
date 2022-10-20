"""

숫자 카드 게임

"""

m, n = map(int, input("Enter Column and Row : ").split())

print(f"행(가로) : {n}  /  열(세로) : {m}")

for i in range(m) : 
    numlist = list(map(int, input("Enter num : ").split()))
    if len(numlist) != n :
        print("Wrong !!!")
        exit()
    numlist.sort()
    result = numlist[0]

print(result)