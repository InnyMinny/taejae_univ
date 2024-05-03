import random

def roll_dice():
    return random.randint(1, 6)

def get_players():
    num = int(input("게임에 참여할 플레이어 수를 입력하세요: "))
    players = []
    for i in range(num):
        name = input(f"플레이어{i+1}의 이름을 입력하세요: ")
        players.append({"name": name, "score": 0})
    return players

def game(players):
    for player in players:
        input(f"""
{player['name']}님, 주사위를 굴리기 위해 Enter키를 누르세요.""")
        score = roll_dice()
        player['score'] = score
        print(f"{player['name']}님이 획득한 주사위 숫자: {score}")

def scores(players):
    print("""
플레이어들의 점수를 공개합니다.""")
    for player in players:
        print(f"{player['name']}: {player['score']}점")

def winner(players):
    biggest = max(player['score'] for player in players)
    winner = [player['name'] for player in players if player['score'] == biggest]
    print(f"{winner}님은 {biggest}점을 획득하여 우승자가 되었습니다.")

def main():
    while True:
        print("""주사위 굴리기 게임에 오신 여러분들 환영합니다
주사위를 굴려 가장 큰 수를 획득한 플레이어가 우승자가 됩니다.
""")
        players = get_players()
        game(players)
        scores(players)
        winner(players)
        print("게임이 종료되었습니다.")
        a = input("""
게임을 다시 시작하려면 y를 입력하고, 종료하려면 n을 입력하세요: """)
        if a == 'y':
            continue
        elif a == 'n':
            print("이용해주셔서 감사합니다")
            break
print(main())