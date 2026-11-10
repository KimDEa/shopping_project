import random
import time

# 가위 바위 보 게임

print("="*30)
print("가위 / 바위 / 보 게임")
print("="*30)

player_total = 0
computer_total = 0

def RSP_game():
    global player_total, computer_total
    table = ["가위", "바위", "보"]
    turn = 3

    name = str(input("플레이어의 이름을 정해주세요.: "))
    # 이기는 경우: 1 : 3, 2 : 1, 3 : 2
    # 지는 경위: 1 : 2, 2 : 3, 3 : 1
    print("게임을 시작합니다.\n")
    time.sleep(1)

    while True:
        if player_total >= 2 or computer_total >= 2:
            print(f"총합 스코어  {name} {player_total} : {computer_total} 컴퓨터")
            if player_total > computer_total:
                print(f"***이번판 {name} 승리***\n")
            elif player_total < computer_total:
                print("***이번판 컴퓨터 승리***\n")
            elif player_total == computer_total:
                print("***이번판 무승부***\n")

            quit = str(input("다시 도전 (yes/no) : "))
            if quit == "yes":
                turn = 3
                player_total = 0
                computer_total = 0
                continue
            else:
                print("게임을 종료합니다.")
                break
        elif turn == 0:
            print("이번판 무승부")
            quit = str(input("다시 도전 (yes/no) : "))
            if quit == "yes":
                turn = 3
                player_total = 0
                computer_total = 0
                continue
            else:
                print("게임을 종료합니다.")
                time.sleep(1)
                break
        else:
            print("1. 가위 / 2. 바위 / 3. 보")
            my_turn = int(input("번호를 선택하세요. : "))
            if my_turn > 3 or my_turn < 1:
                while True:
                    print("보기안에 있는 숫자를 하나만 입력해주세요.")
                    my_turn = int(input("번호를 선택하세요. : "))
                    if my_turn <= 3 and my_turn >= 1:
                        break
            print()
            random_com = random.randint(1, 3)
            if my_turn == 1 and random_com == 3:
                print("[게임 결과]")
                print(f"{name}: {table[my_turn-1]} vs 컴퓨터: {table[random_com-1]}")
                print(f"=> {name} 승리.")
                player_total += 1
                print(f"현재 스코어  {name} {player_total} : {computer_total} 컴퓨터\n")
            elif my_turn == 2 and random_com == 1:
                print("[게임 결과]")
                print(f"{name}: {table[my_turn-1]} vs 컴퓨터: {table[random_com-1]}")
                print(f"=> {name} 승리.")
                player_total += 1
                print(f"현재 스코어  {name} {player_total} : {computer_total} 컴퓨터\n")
            elif my_turn == 3 and random_com == 2:
                print("[게임 결과]")
                print(f"{name}: {table[my_turn-1]} vs 컴퓨터: {table[random_com-1]}")
                print(f"=> {name} 승리.")
                player_total += 1
                print(f"현재 스코어  {name} {player_total} : {computer_total} 컴퓨터\n")
            elif my_turn == 1 and random_com == 2:
                print("[게임 결과]")
                print(f"{name}: {table[my_turn-1]} vs 컴퓨터: {table[random_com-1]}")
                print("=> 컴퓨터 승리.")
                computer_total += 1
                print(f"현재 스코어  {name} {player_total} : {computer_total} 컴퓨터\n")
            elif my_turn == 2 and random_com == 3:
                print("[게임 결과]")
                print(f"{name}: {table[my_turn-1]} vs 컴퓨터: {table[random_com-1]}")
                print("=> 컴퓨터 승리.")
                computer_total += 1
                print(f"현재 스코어  {name} {player_total} : {computer_total} 컴퓨터\n")
            elif my_turn == 3 and random_com == 1:
                print("[게임 결과]")
                print(f"{name}: {table[my_turn-1]} vs 컴퓨터: {table[random_com-1]}")
                print("=> 컴퓨터 승리.")
                computer_total += 1
                print(f"현재 스코어  {name} {player_total} : {computer_total} 컴퓨터\n")
            else:
                print("[게임 결과]")
                print(f"{name}: {table[my_turn-1]} vs 컴퓨터: {table[random_com-1]}")
                print("=> 무승부")
                print(f"현재 스코어  {name} {player_total} : {computer_total} 컴퓨터\n")
            turn -= 1

if __name__ == "__main__":
    RSP_game()