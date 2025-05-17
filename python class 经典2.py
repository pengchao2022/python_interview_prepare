class Dog:
    legs_num = 4
    has_hair = True
    has_tail = True

    def bark(self):
        print("it can say words")
        print(f"this is {self.name}")
    
    def bite(self, person):
        print(f"{self.name} can bite {person}")

    def skill(self):
        print(f"{self.name} can pick up balls")

    def info(self):
        print(f"color:{self.color}")
        print(f"name:{self.name}")
        print(f"weight:{self.weight}")
        print(f"age:{self.age}")
        print(f"height:{self.height}")

dog1 = Dog()

dog1.name = "niujin"
dog1.color = "yellow"
dog1.age = 5
dog1.weight = 40
dog1.height = 46

dog1.info()
