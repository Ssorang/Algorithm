"""

1이 될 때까지

N에서 1을 뺀다.
N을 K로 나눈다.

"""

n, k = map(int,input("Enter num N and K : ").split())

count = 0

while n != 1:
    if n % k == 0:
        n = n // k
        
    else :
        n -= 1

    count += 1

print(count)
