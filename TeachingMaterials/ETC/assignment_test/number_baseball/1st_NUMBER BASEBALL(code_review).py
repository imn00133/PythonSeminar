# #모듈(파일의 이름)은 pep8(name convention)에 의거해 소문자+underscore로 나타내는 것이 좋습니다.
# #import 문은 상단에 붙이는 것이 보기 좋음.

import random

#컴퓨터 난수 생성
while True:
    # #컴퓨터가 잘 하는 것은 반복
    # #이것을 어떻게 반복으로 나타낼 수 있을까?
    # #set을 사용하지 않고, 중복된 값을 어떻게 뽑을 수 있을까?
    # #, 뒤는 한 칸 뛰는 것이 pep8에 맞다.
    a = random.randrange(0,9)
    b = random.randrange(0,9)
    c = random.randrange(0,9)
    d = random.randrange(0,9)
    # #= 앞 뒤로는 공백 한 칸을 주는 것이 pep8에 맞다.
    cnumlist =  [a,b,c,d]
    set_comp = set(cnumlist)
    if len(set_comp) != len(cnumlist):
        # #파이썬의 들여쓰기는 탭 또는 공백 4칸으로, 2칸은 convention에 맞지 않다.
      continue
    else:
      cnumlist = [str(i) for i in cnumlist]
      break
# #제어의 흐름이 이렇게 나눠지면 보기 어렵다.
# #난수 생성이 함수 아래로 내려가면 흐름을 이해하기 편하다.

#점수 확인
result = []
# #사용하지 않는 a, b는 왜 인수로 받는가?
# #pep8에 따르면 함수의 위쪽에는 2칸의 공백을 둔다.
# #함수 내에서 user_input과  cnumlist, trial을 사용하나, 인수로 받지 않는다.
def calc(a,b):
    while True:
        strike = 0
        ball = 0
        out = 0
        # #자세히 보면 반복한다. 이를 간단하게 처리할 수 없을까?
        if user_input[0] == cnumlist[0]:
            strike += 1
        elif user_input[0] in cnumlist:
            ball += 1
        else:
            out += 1

        if user_input[1] == cnumlist[1]:
            strike += 1
        elif user_input[1] in cnumlist:
            ball += 1
        else:
            out += 1

        if user_input[2] == cnumlist[2]:
            strike += 1
        elif user_input[2] in cnumlist:
            ball += 1
        else:
            out += 1

        if user_input[3] == cnumlist[3]:
            strike += 1
        elif user_input[3] in cnumlist:
            ball += 1
        else:
            out += 1

        result.append(strike)
        result.append(ball)
        result.append(out)


        # #흐름을 분리하기 위해 한 칸을 뛸 수 있으나, 두 칸은 pep8에 따르면 많다.
        # #마찬가지로 들여쓰기는 4칸으로
        # #calc이 종료되었을 때, main(사용자 입력값 수집 및 게임시작)부분이 종료되었는지 알지 못한다.
        # #이로 인해, 종료하지 못하고 계속 반복한다.
        # #그렇다면 게임이 종료되었는지 알려면 어떻게 해야할까?
        # #무언가를 반환해주면 되지 않을까?
        if strike == 4:
          print("The End")
          # #fstring은 좋으나, 3.6부터 사용되었으니, 가끔 python버전이 오래되면 안 되는 경우가 있다.
          print(f"{trial}번 만에 끝났습니다.")
          break

        # #원하는 출력은 strike: x, ball: y, out: z였다. 이를 나타내려면?
        # #사용자가 보았을 때 보기 편하게 만들어주는 것도 중요하다.
        else:
          print(strike, ball, out)
          break

print(cnumlist)


#사용자 입력값 수집 및 게임시작
trial = 0
while True:
    # #모든 들여쓰기는 4칸
  user = input("4자리 수를 입력해주세요: ")
  if len(user) != 4:
    print("4자리로 입력해주세요")
    continue
  else:
      # str을 list()를 통해 변환하면 어떨까?
    user_input = [user[0], user[1], user[2], user[3]]
    set_user = set(user_input)

  if len(set_user) != len(user_input):
    print("중복되지 않은 4자리를 입력해주세요")
    continue

  else:
    trial = trial + 1
    calc(user_input, cnumlist)



