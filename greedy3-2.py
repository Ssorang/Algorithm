"""

큰 수의 법칙

"""

n, m, k = map(int, input("Enter n, m, k : ").split())

data = list(map(int, input("Enter num list : ").split()))

data.sort()

first = data[n-1]
second = data[n-2]
sum, count = 0, 0

while count != m :
    for i in range(k) :
        sum = sum + first
        count += 1
    sum = sum + second
    count += 1


print(sum)







