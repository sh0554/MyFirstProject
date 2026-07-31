def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


print("===== Python 계산기 =====")

num1 = int(input("첫 번째 숫자: "))
operator = input("연산자 입력 (+ - * /): ")
num2 = int(input("두 번째 숫자: "))


if operator == "+":
    result = add(num1, num2)

elif operator == "-":
    result = subtract(num1, num2)

elif operator == "*":
    result = multiply(num1, num2)

elif operator == "/":
    result = divide(num1, num2)

else:
    result = "지원하지 않는 연산자입니다."


print("결과:", result)