# 반복적으로 구현한 재귀함수

def factorial_iterative(n):
    result = 1
    for i in range(result,n+1):
        result = result * i
    return result

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

print("반복으로 작성 :: ", factorial_iterative(5))
print("재귀로 작성 :: ", factorial_recursive(5))