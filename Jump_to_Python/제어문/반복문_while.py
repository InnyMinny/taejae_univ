# 문장을 반복해서 수행해야 할 경우 while 문을 사용한다.
# 조건문이 참인 동안 while 문에 속한 문장들이 반복해서 수행된다, 거짓일 때 종료

# ‘열 번 찍어 안 넘어가는 나무 없다’
# treehit = treehit + 1 / treehit += 1
treehit = 0
while treehit < 10:
    treehit = treehit + 1
    print(f"나무를 {treehit}번 찍습니다")
    if treehit == 10:
        print("나무가 넘어갔습니다")

prompt = """
# 1. Add
# 2. Del
# 3. List
# 4. Quit """
number = 0
while number != 4:
    print(prompt)
    number = int(input("Enter number: "))

# while문 강제종료하기: break 이용
# coffee = 10
# money = 300
# while money:
#     print("돈을 받았으니 커피를 줍니다.")
#     coffee -= 1
#     print("남은 커피의 양은 %d개입니다." % coffee)
#     if coffee == 0:
#         print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
#         break
# coffee = 10

# while True:
#     money = int(input("돈을 넣어주세요: "))
#     if money == 300:
#         print("커피를 줍니다")
#         coffee -= 1
#     elif money > 300:
#         print(f"커피와 거스름돈 {money - 300}을 줍니다")
#         coffee -= 1
#     else:
#         print("돈을 다시 돌려주고 커피는 주지 않습니다.")
#         print(f"남은 커피는 {coffee}개 입니다")
#     if coffee == 0:
#         print("커피가 다 떨어졌습니다")
#         break

# while문을 빠져나가지 않고 while문의 맨 처음(조건문)으로 다시 돌아가게 만들고 싶은 경우: continue 사용
# 1부터 10까지의 숫자 중에서 홀수만 출력
a = 0
while a < 10:
    a += 1
    if a % 2 == 0: #a가 짝수이면 다시 처음으로 돌아가고 홀수이면 print된다
        continue
    print(a)
a = 0
while a < 10:
    a += 1
    if a % 2 == 0:
        pass
    print(a)
print("프로그램 다 끝")

# 무한루프: while True
# while True:
#     print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")