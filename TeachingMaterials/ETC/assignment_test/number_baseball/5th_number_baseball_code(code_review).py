"""
docstring에 대해서 알아보자.
정해진 규약은 크게 없으나,
모듈(파일)이나 함수의 맨 상위에 있는 이러한 string을 docstring이라고 부른다.
보통 맨 첫줄은 모듈/함수의 한 줄 요약
그 하위에는 설명을 적는다.(함수내용이나 반환값 등)
doctstring을 사용할 경우, help를 통해 내용을 볼 수 있다.
interactive 창에서
import random
help(random)을 쳐보자.
이것이 docstring을 사용하는 이유이다.
"""

import random

# 함수 목록: game, loop, calc, retrial, usergen, comgen

# game()은 loop가 True면 게임을 재시작. Loop가 False이면 게임을 종료함.
# loop()는 calc()와 retrial()을 하위함수로 가지고, calc와 retrial이 둘 모두 충족되어 True를 반환하기 전까지는 계속 무한반복됨.
# calc()는 com과 user를 가져와서 strike 수를 계산하고, strike 수가 4개면 True를 반환함.
# retrial()은 calc()가 True를 반환해야만 호출됨. 사용자 입력이 y나 n이 들어올 때까지 무한반복되며, y/n에 따라 각각 True/False를 반환.

# calc()와 retrial()이 모두 True면 Loop도 True를 반환하고, game()이 재시행됨.
# calc()는 True고 retrial()이 False면 loop는 종료되며 False를 반환함.

# # 아직까지 game과 loop를 사용하는 이유가 명확하지 않다.
# # 왜 둘을 나눈거지?
# # loop의 종료조건이 매우 복잡해졌다. 이를 어떻게 막아야 될까?

def game():
    while True:
        # # trial이 있는 이유는?
        trial = 0
        com = comgen()
        print(com) # 디버깅용
        if loop(com):
            continue
        break


def loop(com):
    trial = 0
    while True:
        user = usergen()
        trial += 1
        if calc(user, com, trial):
            if retrial():
                return True
            return False


def calc(user, com, trial):
    """
    docstring이다.
    :param user:
    :param com:
    :param trial:
    :return:
    """
    strike = ball = out = 0
    # # a라는 변수를 두는 이유는?
    # # 두었을 때 코드의 이해가 더 편한가?
    a = len(user)
    for i in range(a):
        if user[i] == com[i]:
            strike += 1
        elif user[i] in com:
            ball += 1
        else:
            out += 1

    print(f"strike: {strike}, ball: {ball}, out: {out}")
    # # magic number는 사용하지 않는 것이 좋다.
    # # magic number라는 것은 코드를 읽으면서 이 숫자가 왜 나왔는지 알 수 없는 것을 뜻한다.
    # # 이번 프로그램에서는 4를 사용하니 문제가 없으나, 유연성을 위해서는 상수를 사용하는 것을 추천한다.
    # # 만약에, 내가 5개로 숫자를 바꾸고 싶다고 하면 어떻게 할 것인가?
    if strike == 4:
        # # trial을 여기서 사용하는 이유는?
        print(f"{trial}번 만에 성공했습니다.")
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
        user_input = input("4자리 수를 입력해주세요: ")
        if len(user_input) != 4:
            print("4자리로 입력해주세요")
            continue
        # # 사람마다 다르겠지만 여기서 else를 쓰면 혼돈이 올 수 있다.
        # # if ~ else구문은 보통 if가 아니면 else를 사용한다는 구문으로 사용한다.
        # # 사람이 처리하는 것을 생각해 보았을 때 if문과 else문이 있다면 A가 아니면 B가 처리된다고 생각할 수 있어 혼돈을 줄 수 있다.
        # # 상위 if문은 예외처리이고 하위 문장은 현 함수에서 꼭 사용되야 되는 것이다.
        # # else: 없이 항상 실행되는 문으로 표현하는 것이 이해하기 좋다.
        # # 꼭은 아니지만, 사람이 코드를 읽을 때 생각을 덜어주는 방향으로 구현하는 것이 좋다.
        else:
            # list로 꼭 바꿀 필요는 없다. user_input을 user에 넣어도 잘 작돈한다.
            user = list(user_input)
            user = [int(i) for i in user]
            set_user = set(user)
        if len(set_user) != len(user):
            print("중복되지 않은 4자리를 입력해주세요")
            continue

        return user

def comgen():
    # # pep8에 따르면 함수 앞 뒤는 두 칸의 엔터를 둔다.
    raw = list(range(10))
    raw = [int(i) for i in raw]
    com = random.sample(raw, 4)
    return com


if __name__ == '__main__':
    # # pep8에 따르면 맨 마지막은 빈 엔터를 하나 둔다.
    game()