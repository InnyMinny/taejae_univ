n = int(input("""n번째 피보나치 수를 출력하는 프로그램입니다
n에 들어갈 숫자를 입력해주세요: """))
def fibonacci(n):
    if n == 1:
        print("1번쨰 피보나치 수는 0입니다.")
        return 0
    elif n == 2:
        print("2번째 피보나치 수는 1입니다.")
        return 1
    else:
        value = fibonacci(n-2) + fibonacci(n-1)
        print(f"{n}번째 피보나치 수는 {value}입니다")
        return value
fibonacci(n)
# n = 4부터 오류가 생기는데 뭐가 문제인지 잘 모르겠습니다.