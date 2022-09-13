class Calc():

    def set_number(self, a, b):
        self.a = a
        self.b = b
        self.plus = f"더하기 : {a + b}"
        self.minus = f"빼  기 : {a - b}"
        self.multiple = f"곱하기 : {a * b}"
        self.divide = f"나누기 : {a / b}"

calc = Calc()
calc.set_number(20, 10)

print(calc.plus)
print(calc.minus)
print(calc.multiple)
print(calc.divide) 
