# 숫자형
# 1. int: integer(정수)
a = 123
b = 1_00_000
c = -67
d = 0
print(a, b, c, d)
print(type(d))

# 2. float(실수)
f = 1.2
g = -2.9
e = 4.24E10 #4.24 * 10의 제곱
print(e)
print(type(e))

# 3. 0o: octal(8진수)
o = 0o177
print(o)
print(type(o))

# 4. 0x: hexadecimal(16진수)
x = 0xABC #A:10, B:11, C:12
print(x)
print(type(x))

a = 3
b = 4
# 사칙연산: + - * /
print(a + b)
print(a - b)
print(a * b)
print(a / b)
# 제곱: **
print(a ** b)
print(b ** a)
# 나머지 리턴: %
print(b % a)
# 몫 리턴: //
print(19 // 6)

# 복합 연산자