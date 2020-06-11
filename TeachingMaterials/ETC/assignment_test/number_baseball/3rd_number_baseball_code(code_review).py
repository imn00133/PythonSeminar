import random 


def game():
    # # pep8에 의거하면 함수는 앞에 두 칸의 공백을 주도록 함
    # game loop
    while True: 
        com = comgen()  # 컴퓨터 4자리
        print(com) # 디버깅용

        if loop(com):
            continue
        
        break

def loop(com):
    # strike가 4개가 될 때까지 사용자 입력값을 반복해서 요구하고, 반환된 횟수를 저장
    
    trial = 0
    while True:  
        user, trial = usergen(trial)
        print(user)   # 디버깅용 
        result = calc(com, user)
        
        # 다시 플레이 의사 묻기
        # # result를 받아서 꼭 재 점검을 해야할까?
        if result[0] == 4: 
            print(f"{trial}번 만에 성공했습니다.")
            while True: 
                retry = input("다시 하시겠습니까?(y/n):  ")
                if retry == 'y':
                    return True
                elif retry == 'n':
                    # # return 반환값은 왜 없나?
                    return
                # # countinue가 꼭 필요할까?
                else: 
                    continue
        elif result[0] != 4:  
            print("실패")
            # # 여기의 continue가 꼭 필요할까?
            continue

def calc(com, user):
    # 점수 확인
    # 스트라이크, 볼, 아웃
    # # 변수명은 x, y, z로 쓰면 좋지 않다. 변수명만 가지고도 이게 무슨 말인지 이해할 수 있도록 만드는 것이 좋다.
    # # 지금은 프로그램이 크지 않아 괜찮지만, 프로그램이 커진다면, 함수명을 좀 더 이해하기 쉽게 만드는 것이 좋다.
    # # x = y = z = 0 으로 초기화할 수 있다.
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
    # # 꼭 result를 되돌려줘야 할까?
    result = [x,y,z]
    return result

def usergen(trial):
    # 사용자 입력값을 받으면서, 입력값을 받을 때마다 횟수 +1 
    while True:
        user_input = input("4자리 수를 입력해주세요: ")
        if len(user_input) != 4:
            print("4자리로 입력해주세요")
            continue
        else:
            # # user_input[0]으로 list를 만들지 않아도 된다.
            # # list(str)을 하면 각 문자별로 list가 만들어진다.
            # # 여기에 else문을 사용한 까닭은?
            # # 사람마다 다르겠지만, 여기서 else문을 꼭 사용할 필요는 없다.
            # # if ~ else문을 생각해보면 if가 아니면 else를 해달라는 것이다.
            # # 그런데 여기서 if문은 예외처리를 하는 것으로 본다면, else문이 꼭 필요한지 생각해 봐야 한다.
            # # 프로그램의 수행 흐름상 if 예외 처리 후,
            # # 무조건 실행되어야 되는 문으로 이해하려면 else가 없는게 좋지 않을까 싶다.
            user = [user_input[0], user_input[1], user_input[2], user_input[3]]
            set_user = set(user)
        if len(set_user) != len(user):
            print("중복되지 않은 4자리를 입력해주세요")
            continue
        else:
            # # indent는 4칸
          trial += 1
          return user, trial

def comgen():
    # # 여기에 while True가 필요한 까닭은?
    while True: 
        raw = list(range(10))
        raw = [str(i) for i in raw]
        com = random.sample(raw, 4)
        return com

if __name__ == '__main__':
    game()