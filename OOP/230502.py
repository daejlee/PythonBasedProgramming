import math as m

class Circle:
    def __init__(self, name, inputRadius):
        self.radius = inputRadius
        self.name = name
    def getArea(self):
        return m.pow(self.radius, 2) * m.pi
    def getPerimeter(self):
        return 2 * m.pi * self.radius
    
class Car:
    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model
        print("자동차 객체를 생성하였습니다.")
    def __str__(self):
        return f'Car(model={self.model}, color={self.color}, speed={self.speed})'
    def print_speed(self):
        print(f'자동차의 속도는 {self.speed}')
    def print_color(self):
        print(f'자동차의 색상은 {self.color}')
    def print_model(self):
        print(f'자동차의 모델은 {self.model}')

#dict속성을 이용해 인스턴스변수와 값을 알아본다.
c1 = Circle("C1", 4)
print(c1.__dict__)
#__str__() 메소드를 이용하여 어떤 객체의 문자열 표현 방식을 정의.
car1 = Car(60, "Red", "porche")
print(car1)

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'{self.x}, {self.y}'
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
a = Vector2D(10, 20)
b = Vector2D(30, 40)
c = a + b
print(c)
