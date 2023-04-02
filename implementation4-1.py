"""

구현 

"""


from distutils.file_util import move_file


n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        
        x, y = nx, ny

print(x, y)

"""

size = map(int,input("Enter num SIZE : ").split())
move = list(map(str, input("Enter string MOVE : ").split()))

print(f"size = {size}, move = {move}")

row, col = 1, 1

if row or col < size :
    for m in move :
        
        if m == "R" :
            row += 1

        elif m == "L" :
            row -= 1

        elif m == "U" :
            col -= 1

        elif m == "D" :
            col += 1

        else :
            print("Wrong !!!")
        
        if row == 0:
            row = 1

        elif col == 0:
            col = 1

print(col,row)

"""
