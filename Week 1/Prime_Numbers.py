print("소수판별기")
pn = int(input("숫자를 입력하세요: "))
a = 0
if pn < 2:
    print(f"""{pn}은/는 소수가 아닙니다. 소수는 2보다 크거나 같아야 합니다.
프로그램을 다시 실행해주세요.""")
else:
    for i in range(2, pn):
        result = pn % i
        if result == 0:
            a = a + 1
    if a == 0:
        print(f"{pn}은(는) 소수입니다.")
    else:
        print(f"{pn}은(는) 소수가 아닙니다.")
