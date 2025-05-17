
class Dog:
    legs_num = 4
    has_hair = True
    has_tail = True

    def bark(self):
        print("it can say words")
    
    def bite(self, person):
        print(f"it can bite {person}")

    def skill(self):
        print("it can pick up balls")

dog1 = Dog()

print(dog1.has_hair)
dog1.skill()
dog1.bite()
dog1.bark()

dog2 = Dog()
print(id(dog1))
print(id(dog2))

print(dog1 == dog2)


print(id(dog1.legs_num))

print(id(dog2.legs_num))

print(id(dog1.bite))
print(id(dog2.bite))

dog1.name = "kate"
dog1.age = 9

print(dog1.name)

dog1.age = 20

print(dog1.age)

dog1.legs_num = 8
print(dog1.legs_num)

dog1.bite("iu")

