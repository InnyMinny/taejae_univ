n = int(input("""n번째 피보나치 수를 출력하는 프로그램입니다
n에 들어갈 숫자를 입력해주세요: """))
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)
answer = fibonacci(n)
print(f"{n}번째 피보나치 수는 {answer}입니다")