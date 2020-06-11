import random
# # docstring은 맨 위에 import가 아래로 가야함, 최상단
'''
사용되는 함수: game(), loop(), calc(), retrial(), comgen(), usergen()

game()은 하위함수로 loop()를 가진다. loop()은 strike가 4개가 될 때까지 calc()함수를 통해 결과를 확인하고, usergen()을 반복토록 하는 함수이다. 
calc함수가 True를 반환하면 loop()를 빠져나온다. 


game()은 loop()가 False를 반환하게 되면 retrial()을 통해 사용자의 반복 의사를 묻는다. 다시 반복하길 원하는 경우 True를 반환하고, 종료를 원할 시 
False를 반환한다. True일 경우 game()의 루프가 반복된다. 
'''
# # docstring이 너무 깁니다. pep8에 따르면 79자정도로 이야기를 함.
# # docstirng의 의미를 따르고 있긴 하나, 좀 더 정제하면 좋긴 함.
# # 뭐 재사용성이 지금 파일에서는 없으니, docstring을 꼭 처리할 필요는 없지.
# # 주석을 달 때 주의할 점은, 파일이 갱신되면 같이 갱신시켜야 함.
# # 지금은 주석과 내용이 맞지 않지?


def game():
    while True:
        com = comgen()
        print(com) # 디버깅용
        loop(com)
        if retrial():
            continue
        break


def loop(com):
    trial = 0
    while True:
        user = usergen()
        trial += 1
        if calc(user, com, trial):
            break


def calc(user, com, trial):
    strike = ball = out = 0
    for i in range(len(user)):
        if user[i] == com[i]:
            strike += 1
        elif user[i] in com:
            ball += 1
        else:
            out += 1

    print(f"strike: {strike}, ball: {ball}, out: {out}")

    if strike == len(user):
        # # 뭐 그정도는..
        # # 사실 고려해보면, parameter를 늘리는 것 보다는 loop에서 처리하는 것이 보기 좋긴 하지.
        print(f"{trial}번 만에 성공했습니다.")   # trial을 여기서 사용하는 이유는...그냥 개인적인 취향??
        return True


def retrial():
    while True:
        retry = input("다시 하시겠습니까?(y/n):  ")
        if retry == 'y':
            return True
        elif retry == 'n':
            return False


def usergen():
    # 사용자 입력값을 받으면서, 입력값을 받을 때마다 횟수 +1
    while True:
        user = input("4자리 수를 입력해주세요: ")
        if len(user) != 4:
            print("4자리로 입력해주세요")
            continue

        user = [int(i) for i in user]
        set_user = set(user)
        if len(set_user) != len(user):
            print("중복되지 않은 4자리를 입력해주세요")
            continue

        return user


def comgen():
    raw = list(range(10))
    raw = [int(i) for i in raw]
    com = random.sample(raw, 4)
    return com


if __name__ == '__main__':
    game()
