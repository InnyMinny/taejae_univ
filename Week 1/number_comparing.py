print("가장 큰 숫자를 출력합니다, 서로 다른 숫자 3개를 1개씩 입력해주세요.")
a = int(input("숫자 1: "))
b = int(input("숫자 2: "))
c = int(input("숫자 3: "))
if a > b and a > c:
    print(a)
elif b > c:
    print(b)
else:
    print(c)
