# for문 활용
n = int(input("n!의 n을 입력하세요: "))
factorial = 1
for i in range(1, n+1, 1):
    factorial = factorial * i
print(f"{n}! =", factorial)

# while문 활용
n = int(input("n!의 n을 입력하세요: "))
factorial = 1
while n >= 1:
    factorial = factorial * n
    n = n - 1
print(factorial)