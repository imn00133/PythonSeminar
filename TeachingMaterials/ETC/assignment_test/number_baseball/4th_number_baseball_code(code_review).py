import random


def game():
    # game loop
    # # game과 loop의 차이점은 무엇일까?
    # # game()는 무엇을 하길 의도했고, loop는 무엇을 하길 의도했을까.
    # # 분리해야 되는 걸까? 왜 나눠진거지?
    while True:
        com = comgen()  # 컴퓨터 4자리
        print(com)  # 디버깅용

        if loop(com):
            continue
        break


def loop(com):
    trial = 0
    while True:
        user, trial = usergen(trial)
        print(user)  # 디버깅용
        calc(com, user, trial)
        break


def calc(com, user, trial):
    # 점수 확인
    # 스트라이크, 볼, 아웃
    strike = ball = out = 0

    for i in range(4):
        # # 항상 지켜져야 되는 건 아니지만, magic number는 좋지 않다.
        # # 만약에 갑자기 4자리가 아니라 5자리를 하고 싶다면?
        if user[i] == com[i]:
            strike += 1
        elif user[i] in com:
            ball += 1
        else:
            out += 1

    print(f"strike: {strike}, ball: {ball}, out: {out}")
    # # 꼭 그렇지는 않지만, 함수는 하나의 기능을 하는게 좋다.
    # # 이 함수는 점수 확인 함수인데, 여기서 꼭 물어보아야 할까?
    if strike == 4:
        print(f"{trial}번 만에 성공했습니다.")
        while True:
            retry = input("다시 하시겠습니까?(y/n):  ")
            if retry == 'y':
                return True
            elif retry == 'n':
                return False
    elif strike != 4:
        print("실패")


def usergen(trial):
    # 사용자 입력값을 받으면서, 입력값을 받을 때마다 횟수 +1
    while True:
        user_input = input("4자리 수를 입력해주세요: ")
        if len(user_input) != 4:
            print("4자리로 입력해주세요")
            continue
        else:
            user = list(user_input)
            set_user = set(user)
        if len(set_user) != len(user):
            print("중복되지 않은 4자리를 입력해주세요")
            continue
        # # trial이 여기서 꼭 횟수가 증가되어야 할까?
        # # 여기서 trial이 하는 역할은?
        trial += 1
        return user, trial


def comgen():
        raw = list(range(10))
        raw = [str(i) for i in raw]
        com = random.sample(raw, 4)
        return com


if __name__ == '__main__':
    game()
