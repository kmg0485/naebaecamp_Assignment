"""
#내가 짜본 코드

from random import randint
import time
from datetime import datetime



def unique(x): #중복입력방지를 위한 함수
    for i in x:
        if(x.count(i)>=2):
            return False
    return True

start_time = time.time()
baseball = True



while baseball:
    count = 0
    n = 0
    
    try: n=int(input("몇자리수인지 입력하시오.(1~10)"))
        
    except ValueError:
        print("숫자를 입력하시오.")
        break
        
        
    if n > 10 :
        print("1~10까지 정수만")
        
    elif n <=10 :
        num=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        guess = []
        for i in range(n):
            temp = randint(0, len(num)-1)
            guess.append(num[temp])
        print(guess)
        print("띄어쓰기 하지말고 0~9사이의 숫자들을 적으시오.")
        
        baseball2 = True
        while baseball2:
            count+=1
            usr_guess = str(input("숫자를 맞혀보세요."))
            try: temp=int(usr_guess)
            
            except ValueError:
                if usr_guess == 'exit':
                    baseball2 = False
                    baseball = False
                
            if len(usr_guess) != n:
                print(n, "자리 숫자입니다.")
            
            elif not unique(usr_guess):
                print("\n 중복은 안됩니다.")
                
            elif True :
                strike = 0
                ball = 0
                out = 0
                for i in range(n):
                    if usr_guess[i] == guess[i]:
                        strike += 1
                    elif usr_guess[i] in guess:
                        ball += 1
                    elif not usr_guess[i] in guess:
                        out += 1
                if strike == n:
                    end_time = time.time()
                    print(f"축하합니다. {count} 번 만에 정답입니다! 소요시간:{end_time-start_time:.2f}초 {datetime.now()}")
                    baseball2 = False
                    baseball = False
                else:
                    print(f"\n {strike} 스트라이크, {ball} 볼, {out} 아웃")
"""



"""
#다른 분이 짠 코드

import random
import time
from datetime import datetime, timedelta
print("원하시는 자리 수를 입력하세요")
n = int(input())
start_time = time.time()
def baseball_number_generator(n):
    result = set()
    if n < 1:
        print("1이상의 값을 입력해주세요")
        return False
    while len(result)<n:
        result.add(random.randint(1,9))
    result = list(result)
    random.shuffle(result)
    return result
baseball_numbers = baseball_number_generator(n)
print(baseball_numbers)
def baseball_game():
    try_count = 0
    out_count = 0
    strike_count = 0
    ball_count = 0
    print(f"처음에 입력하셨던 {n} 자리수만큼 한자리씩 띄워서 숫자를 입력하세요")
    try:
        while True:
            if strike_count < 3:
                player_numbers = list(map(int, input().split()))
                try_count +=1
                strike_count = 0
                ball_count = 0
                out_count = 0
                for i in range(len(player_numbers)):
                    if player_numbers[i] in baseball_numbers:
                        if player_numbers[i] == baseball_numbers[i]:
                            strike_count += 1
                        else :
                            ball_count += 1
                    else:
                        out_count += 1
                print(f"{try_count}번 시도했습니다. 스트라이크 : {strike_count}  볼 : {ball_count} 아웃 : {out_count}")
            else:
                end_time = time.time()
                print(f"정답을 맞추기까지 소요된 시간 : {end_time-start_time:.0f}초")
                now = datetime.now()
                string_datimetime = datetime.strftime(now, "%y%m%d %H:%M:%S")
                print(string_datimetime)
                print(baseball_numbers)
                print("게임성공")
                return True
    except:
        print("게임 종료")
baseball_game()

"""

#튜터님이 짠 코드
import random
import time
from datetime import datetime


def main():
    length = int(input("자릿수를 입력해주세요 : "))
    random_numbers = set()

    while len(random_numbers) < length:
        random_numbers.add(random.randint(0, 9))

    random_numbers = list(random_numbers)
    random.shuffle(random_numbers)

    start_time = time.time()
    try_count = 0

    while True:
        input_number = input("값을 입력해주세요 (종료 - exit): ")
        if input_number == "exit":
            return
        
        try_count += 1
        out_count = 0

        ball_count = 0
        strike_count = 0

        for i, v in enumerate(input_number):
            v = int(v)
            if v not in random_numbers: # 포함돼있지 않은 경우
                out_count += 1
                
            else: # 포함돼 있는 경우
                if random_numbers[i] == v:
                    strike_count += 1
                else:
                    ball_count += 1
                    
        if strike_count == length:
            print("########################")
            print("정답입니다!!")
            print(f"소요 시간 : {time.time() - start_time:.2f}")
            print(f"클리어 일자 : {datetime.now()}")
            print(f"도전 횟수 : {try_count}")
            print("########################")
            return
        
        print(f"{ball_count}볼 {strike_count}스트라이크 {out_count}아웃")

main()