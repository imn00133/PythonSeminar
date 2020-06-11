import random

# 게임
def game():
    # #함수에 대한 설명은 함수 위가 아닌 내부, 맨 위에 적는 것이 좋습니다. 이부분
    # #C와는 다르게, 사용하기 전에 꼭 초기화할 필요는 없다.
    # #com, user, reslut, trial은 어쩌피 바로 생성해서 받아오기 때문에, 처음에 꼭 적지 않아도 된다.
    com = []
    user = []
    result = []
    trial = 0
    retry = 0

    com = comgen(com)
    user = usergen(user)
    result, trial = calc(com, user, result, trial)

# 디버깅용 cheatsheet
    print(com)
    print(user)


# 승리조건
    # #함수 내에서 주석을 달 경우, 들여쓰기를 맞춰줘야 함수 내인지 아닌지 확인하기가 편합니다.
    while retry == 0:
        # #이 부분은 복잡하다.
        # #while은 retry에 걸리고, 내부에서는 result를 통해 성공인지 아닌지 확인한다.
        # #좀 더 깔끔하게 바꿀수는 없을까?
        # #왜 retry가 외부에 있는 걸까?
        if result[0] == 4:
            # #들여쓰기는 4칸
          print(f"{trial}번 만에 성공했습니다.")
          retry = input("다시 하시겠습니까?(y/n):  ")
          if retry == 'y':
              # #game내에서 game을 다시 호출하는 것은 좋지 않습니다.
              # #이는 재귀함수와 유사한 방법입니다.
              # #1000번 이상 호출되거나, 그 전에 램을 많이 먹게되면 재귀 한계 또는 stack한계에 도달하면서 오류를 냄
              # #따라서 방법을 바꿔줄 필요가 있음
              game()   

          elif retry == 'n':
              print("종료")
              break

          else:
              # #retry에 아무 값이나 입력되면 다시 묻지 않고 종료된다.
              print("y또는 n을 눌러주세요.")
              continue

        elif result[0] != 4:  
            print("실패")
            user = usergen(user)  
            result, trial = calc(com, user, result, trial)
            continue

# 사용자 입력값 받기
def usergen(user):
    while True:
        user_input = input("4자리 수를 입력해주세요: ")
        if len(user_input) != 4:
            print("4자리로 입력해주세요")
            continue

        else:
            # #magic number로 하드코딩하는 것보다 프로그램의 유연성을 주는게 좋다
            # #다른 방법은 없을까?
            user = [user_input[0], user_input[1], user_input[2], user_input[3]]
            set_user = set(user)

        if len(set_user) != len(user):
            print("중복되지 않은 4자리를 입력해주세요")
            continue

        else:
          return user

# 컴퓨터 난수 생성
def comgen(com):
    while True: 
        com = random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 4)
        return com

# 점수 확인
def calc(com, user, result, trial):
    # #받아온 result는 사용되지 않는다. 인수로 받아올 필요가 없다.
    trial += 1   # 횟수 카운터

    # 스트라이크, 볼, 아웃
    x = 0  
    y = 0
    z = 0
    
    for i in range(4):
        if user[i] == com[i]:
            x += 1
        
        elif user[i] in com:
            y += 1
        
        else: 
            z += 1

    print(f"strike: {x}, ball: {y}, out: {z}")
    result = [x,y,z]
    return result, trial
    
#######################################################################

# #게임을 시작하기 위해 맨 아래에 이렇게 두는 것도 좋으나
# #if __name__ == '__main__':
# #    game()
# #으로 두는 것이 좋다.
game()
