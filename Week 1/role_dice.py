import random

def roll_dice():
    return random.randint(1, 6)

def get_players():
    num_players = int(input("플레이어 수를 입력하세요: "))
    players = []
    for i in range(num_players):
        name = input(f"{i+1}번 플레이어의 이름을 입력하세요: ")
        players.append({"name": name, "score": 0})
    return players

def play_game(players):
    for player in players:
        input(f"{player['name']}님, 주사위를 굴려주세요. (Enter를 누르세요)")
        score = roll_dice()
        player['score'] = score
        print(f"{player['name']}님의 주사위 숫자: {score}")

def print_scores(players):
    print("---- 점수 ----")
    for player in players:
        print(f"{player['name']}: {player['score']}")

def find_winner(players):
    max_score = max(player['score'] for player in players)
    winners = [player['name'] for player in players if player['score'] == max_score]
    print(f"최고 점수: {max_score}")
    print(f"최고 점수를 획득한 플레이어: {', '.join(winners)}")

def main():
    while True:
        players = get_players()
        play_game(players)
        print_scores(players)
        find_winner(players)
        again = input("게임을 다시 시작하시겠습니까? (y/n): ")
        if again.lower() != 'y':
            break

if __name__ == "__main__":
    main()

# print("""주사위 굴리기 게임에 오신 여러분들 환영합니다
# 주사위를 굴려 가장 큰 수가 나온 플레이어가 이깁니다.""")
# num = int(input("게임에 참여하는 인원 수를 입력해주세요: "))
# print(num)
# name = 0
# while name >= 0:
#     name = name + 1
#     player = input(f'플레이어{name}의 이름을 입력하세요: ')
#     dic = {name: player}
#     if name == num:
#         print("주사위 굴리기를 시작합니다.")
#         break
# import random
# def roll_dice():
#     score = random.randint(1, 6)
#     return score