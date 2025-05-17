
class Dog:
    legs_num = 4
    has_hair = True
    has_tail = True

    def bark(self):
        print("it can say words")
    
    def bite(self):
        print("it can bite people")

    def skill(self):
        print("it can pick up balls")

dog1 = Dog()

print(dog1.has_hair)
dog1.skill()
dog1.bite()
dog1.bark()
