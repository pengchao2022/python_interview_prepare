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

dog1 = Dog()

dog1.name = "niujin"

dog1.bite("tim ni")

dog1.bark()

dog1.skill()
