
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

print(iphone12.color, iphone12.price, iphone12.location)

iphone12.play_game()

iphone12.make_call()

iphone12.take_photos()
