
#python中的类方法

#定义一个类
class Person:

    #魔法方法
    #构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #私有方法
    def __eat(self):
        pass

    #对象方法，成员方法
    def run(self):
        pass

    #类方法
    #1,类方法里面有cls, 而静态方法里面没有cls,2, 可以调用类方法和属性
    #2，可以使用类来调用

    @classmethod
    def sing(cls): #cls = class
        pass


    #静态方法
    @staticmethod
    def dance():
        pass
    


        