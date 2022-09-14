
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
    calc.set_number(20, 0)

    
except ZeroDivisionError: 
    print("0으로는 나눌수 없습니다.")
    exit()


print(calc.plus())
print(calc.minus())
print(calc.multiple())
print(calc.divide()) 


#################################################

from pprint import pprint
people = [
    ("Blake Howell", "Jamaica", 18, "aw@jul.bw"),
    ("Peter Bowen", "Burundi", 30, "vinaf@rilkov.il"),
    ("Winnie Hall", "Palestinian Territories", 22, "moci@pacivhe.net"),
    ("Alfred Schwartz", "Syria", 29, "ic@tolseuc.pr"),
    ("Carrie Palmer", "Mauritius", 28, "fenlofi@tor.aq"),
    ("Rose Tyler", "Martinique", 17, "as@forebjab.et"),
    ("Katharine Little", "Anguilla", 29, "am@kifez.et"),
    ("Brent Peterson", "Svalbard & Jan Mayen", 22, "le@wekciga.lr"),
    ("Lydia Thornton", "Puerto Rico", 19, "lefvoru@itbewuk.at"),
    ("Richard Newton", "Pitcairn Islands", 17, "da@lasowiwa.su"),
    ("Eric Townsend", "Svalbard & Jan Mayen", 22, "jijer@cipzo.gp"),
    ("Trevor Hines", "Dominican Republic", 15, "ev@hivew.tm"),
    ("Inez Little", "Namibia", 26, "meewi@mirha.ye"),
    ("Lloyd Aguilar", "Swaziland", 16, "oza@emneme.bb"),
    ("Erik Lane", "Turkey", 30, "efumazza@va.hn"),
]

member = [x for x in people if x[2] >= 20]
member.sort(key = lambda x: x[2])


pprint(member)
