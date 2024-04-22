# for문의 기본구조: 빼와서 넣고 출력하기
# for 변수 in 리스트(또는 튜플, 문자열):
#     수행할_문장1
#     수행할_문장2
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i) # 'one', 'two', 'three'가 순차적으로 하나씩 i에 담겨서 출력됨

# a 리스트의 요솟값이 튜플이기 때문에 각각의 요소가 자동으로 (first, last) 변수에 대입
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last) #(first, last)에 (1,2), (3,4), (5,6)가 순차적으로 들어감-> 3, 7, 11

# 각각의 학생에게 번호를 붙여 주기 위해 number 변수를 사용하였다.
# 점수 리스트 score에서 차례로 점수를 꺼내어 i라는 변수에 대입하고 for문 안의 문장들을 수행한다.
# 먼저 for 문이 한 번씩 수행될 때마다 number는 1씩 증가한다.
score = [90, 25, 67, 45, 80]
number = 0
for i in score:
    number += 1  # 0번 학생이 아니라 1번 학생부터 시작하도록 세팅
    if i >= 60:
        print(f"{number}번 학생은 합격입니다.")
    else:
        print(f"{number}번 학생은 불합격입니다.")

# for문에서 continue 사용
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number +1
    if mark < 60:
        continue # 60점 미만인 경우 다시 처음 for문으로 돌아가고 60점이상인 경우 print됨
    print(f"{number}번 학생 축하합니다. 합격입니다. ")

# range 함수: 범위 나타내기(list을 쭉 쓰기 귀찮을 때)
add = 0
for i in range(1, 11):
    add += i
print(add)

for i in range(1, 10):        # 1번 for문
    for j in range(1, 10):    # 2번 for문
        print(i * j, end=" ")
    print('')
# print(i*j, end=" ")와 같이 print 함수에 end 파라미터를 설정한 이유는
# 해당 결괏값을 출력할 때 다음 줄로 넘기지 않고 그 줄에 계속 출력하기 위해서이다.
# print 문은 줄바꿈 문자(\n)가 기본값으로 설정되어 있다
# print('')는 2단, 3단 등을 구분하기 위해 사용했다.

