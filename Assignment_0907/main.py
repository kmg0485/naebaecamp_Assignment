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