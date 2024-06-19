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
        
        
# p1 = Pet("Sunshine", 4)
# p2 = Pet("Puka", 2)

# print(p1.speak())

# d1 = Dog("Rue", 4, "Morkie")

# print(d1.careForAPet())


class Vehicle:
    numOfVehicles = 0
    
    def __init__(self, owner, year, miles):
        self.owner = owner
        self.year = year
        self.miles = miles
        Vehicle.numOfVehicles += 1
        
    def show(self):
        print("The owner of this vehicle is ", self.owner,
            ". It was made in ", self.year,
            ". It has ", self.miles, " miles on it.")
        
    @classmethod
    def getNumOfVehicles(cls):
        return cls.numOfVehicles
    
class Car(Vehicle):
    numOfCars = 0
    
    def __init__(self, owner, year, miles, make, model):
        super().__init__(owner, year, miles)
        self.make = make
        self.model = model
        Car.numOfCars += 1
        
    def show(self):
        print(f'{self.owner} owns this car. It is a {self.year} {self.make} {self.model}. It has {self.miles} miles on the engine.')
    
    
# v1 = Vehicle("Ari", 2010, 114000)
# v2 = Vehicle("Tommy V", 2006, 251000)

# v1.show()
# v2.show()
# print(Vehicle.numOfVehicles)
# print(Vehicle.getNumOfVehicles())
# print(v1.getNumOfVehicles())
# print(v1.numOfVehicles)

# print("")
# c1 = Car("Tommy", 2014, 95000, "Subaru", "BRZ")

# print(c1.getNumOfVehicles())
# print(c1.numOfVehicles)
# print(c1.numOfCars)
# c1.show()