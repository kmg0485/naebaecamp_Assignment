from calculator import cal, plus, minus, multiply, division

print("두개의 숫자를 공백을 두고 입력시킨 후 연산기호를 입력하시오.")
num1, num2 = map(int,input().split())
oper = input()

print(cal(num1, num2, oper))