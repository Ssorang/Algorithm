N = int(input("Insert Hour (24H) :: "))

count = 0

for h in range(0, N+1) :
    for m in range(60) :
        for s in range(60) :
            if '3' in str(h) + str(m) + str(s) :
                count += 1

print(count)
