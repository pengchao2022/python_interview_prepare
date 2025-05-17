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

dog1.bite("tim ni")
