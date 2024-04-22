# 순서도 그려보기
# indent 제대로 하기!(tab or 띄어쓰기 4칸)
money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")
money = False
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket: pass
else: print("카드를 꺼내라")

# 위에서부터 아래로 실행됨, 순서 제대로 생각해서 짜기!
# else문이 if문이 거짓일 때 사용되는 것처럼 elif는 이전 조건문이 거짓일 때 수행된다.
# elif는 개수에 제한 없이 사용할 수 있다.
score = int(input("enter your score: "))
if score > 100:
    print("invalid score")
elif score == 100:
    print("perfect score!")
elif score >= 90:
    print("A")
else:
    print("not bad")

# 조건부 표현식: 변수 = 조건문이_참인_경우의_값 if 조건문 else 조건문이_거짓인_경우의_값
height = int(input("enter your height: "))
sent = "you can ride" if height >= 140 else "you can't ride"
print(sent)