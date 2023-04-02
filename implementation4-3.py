"""

구현 4-3 

" 왕실의 나이트 "

"""

position = input("Input Knight Position :: ")
col = int(position[1])
row = ord(position[0]) - 96 # a = 97

steps = [[1,2],[1,-2],[-1,2],[-1,-2],[2,1],[2,-1],[-2,1],[-2,-1]]
result = 0

for step in steps:
    next_row = row - step[0]
    next_col = col - step[1]

    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_row <= 8 :
        result += 1

print(result)