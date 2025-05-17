class Dog:
    legs_num = 4
    has_hair = True
    has_tail = True

    def __init__(self, name, age, color, weight, height):
        self.name = name
        self.age = age
        self.color = color
        self.weight = weight
        self.height = height

    def bark(self):
        print("it can say words")
    
    def bite(self, person):
        print(f"it can bite {person}")

    def skill(self):
        print("it can pick up balls")
    
    def show_info(self):
        print(f"名字：{self.name}, 年龄：{self.age}, 颜色：{self.color}, 高度：{self.height}, 重量：{self.weight}")



dog1 = Dog(name='kate', age=18, color="yellow", height=44, weight=78)

dog1.show_info()

