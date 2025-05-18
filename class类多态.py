#多态
#在继承的基础上，一般有多个子类同时继承一个父类，让每个子类去重写父类同一个方法
#子类在这个方法上实现不同的功能，那么用父类对象指向不同子类的时候，调用该方法可以实现不同的功能

#父类
class Animals:
    def eat(self):
        #父类不需要实现
        pass

#子类
class Dog(Animals):
    def eat(self):
        print('吃骨头')

class Cat(Animals):
    def eat(self):
        print('吃老鼠')

class Pig(Animals):
    def eat(self):
        print('吃白菜') 

#调用

class Person:
    def feed(self, Animals):
        Animals.eat()

dog = Dog()
cat = Cat()
pig = Pig()

#调用多态
Person().feed(dog)

Person().feed(cat)

Person().feed(pig)

