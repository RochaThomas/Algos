# python interview prep
# practicing OOP with classes

class Pet:
    numOfPets = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Pet.numOfPets += 1
        
    def speak(self):
        return "I am a pet"
    
    @classmethod
    def getNumOfPets(cls):
        return cls.numOfPets
    
    @staticmethod
    def careForAPet():
        return "Pets need food, water, and love"
    
class Dog(Pet):
    numOfDogs = 0
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
        Dog.numOfDogs += 1
        
    def speak(self):
        return "Bark Bark Bark"
    
    @classmethod
    def getNumOfPets(cls):
        return super().getNumOfPets()
        
        
p1 = Pet("Sunshine", 4)
p2 = Pet("Puka", 2)

print(p1.speak())

d1 = Dog("Rue", 4, "Morkie")

print(d1.careForAPet())