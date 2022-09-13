
class Square_area():
    def __init__(self, width, height):
        print(f"사각형의 넓이는 {width * height}입니다.")
        # self.width = width
        # self.height = height

class rec_area():
    def __init__(self, width, height):
        print(f"삼각형의 넓이는 {width * height // 2}입니다.")
        # self.width = width
        # self.height = height

class cir_area():
    def __init__(self, width):
        PIE = 3.14
        print(f"원의 넓이는 {((width // 2) * (width // 2) * PIE):.2f}입니다.")
        # self.width = width




Square = Square_area(10, 20)
rectangle = rec_area(10, 20)
circle = cir_area(10)


"""
class Cal():
    def __init__ (self, width, height):
        self.width = width
        self.height = height
    def Square_area(self):
        return self.width * self.height
    def Triangle_area(self):
        return self.width * self.height / 2
    def Circle_area(self):
        return (self.width/2)**2 * 3
area = Cal(14,23)
print(area.Square_area())
print(area.Triangle_area())
print(area.Circle_area())
"""

