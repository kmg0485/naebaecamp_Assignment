"""
#calc.set_number 에 0이나 문자 넣어보기.
try:
    class Calc():

        def set_number(self, a, b):
            self.a = int(a)
            self.b = int(b)
            
        def plus(self):
            return f"더하기 : {self.a + self.b}"
        def minus(self):
            return f"빼  기 : {self.a - self.b}"
        def multiple(self):
            return f"곱하기 : {self.a * self.b}"
        def divide(self):
            return f"나누기 : {self.a / self.b}" 
        
    calc = Calc()   
    calc.set_number(20, ㅁㄴㅇㄹㅁㄴㅇㄹ)
    
    print(calc.plus())
    print(calc.minus())
    print(calc.multiple())
    print(calc.divide()) 

    
except ZeroDivisionError: 
    print("0으로는 나눌수 없습니다.")
    exit()
    
except NameError: 
    print("숫자만 입력 가능합니다.")
    exit()
"""
###############################################################

class Calc():

    def set_number(self, a, b):
        self.a = int(a)
        self.b = int(b)
            
    def plus(self):
        return f"더하기 : {self.a + self.b}"
    def minus(self):
        return f"빼  기 : {self.a - self.b}"
    def multiple(self):
        return f"곱하기 : {self.a * self.b}"
    def divide(self):
        try:
            f"나누기 : {self.a / self.b}" 
        except ZeroDivisionError: 
            print("0으로는 나눌수 없습니다.")
            exit()
            
            
            
while True:
    try:
        num1, num2 = [int(x) for x in input().split(" ")]
        break
    except ValueError:
        print("숫자만 입력 가능합니다.")
        exit()
    
    
    
calc = Calc()   
calc.set_number(num1, num2)
    
print(calc.plus())
print(calc.minus())
print(calc.multiple())
print(calc.divide()) 

    