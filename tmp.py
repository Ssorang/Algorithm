"""

Problem 4-13
 - 주어진 정수에서 반복되는 숫자를 제거하는 프로그램을 스택(stack)을 이용하여 작성하시오.
 - 정수 입력: 개발자가 임의의 연속되는 수 입력(예: 1222334)
 * 출력: 1234

"""

stack = []

num = input("임의의 연속되는 수 입력 : ")

for i in num :
    if i in stack :
        stack.pop()
        stack.append(i)
    else :
        stack.append(i)
    print(stack)

print(stack)

