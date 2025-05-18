
#父类
class Ipad(object):
    #超类，根类
    def __init__(self, color):
        self.color = color

    def play_game(self):
        print("可以玩游戏")

    
#子类
class Iphone(Ipad):
    
    def __init__(self, color, price, location, name):
        super().__init__(color)
        self.price = price
        self.location = location
        self.name = name

    def make_call(self):
        print("可以打电话")

    def take_photos(self):
        print(f"{self.name}，可以拍照！")

iphone12 = Iphone('银色', 12000, 'China', 'Iphone12')

print(iphone12.color, iphone12.price, iphone12.location, iphone12.name)

iphone12.play_game()

iphone12.make_call()

iphone12.take_photos()


#多态
#在继承的基础上，一般有多个子类同时继承一个父类，让每个子类去重写父类同一个方法
#子类在这个方法上实现不同的功能，那么用父类对象指向不同子类的时候，调用该方法可以实现不同的功能

