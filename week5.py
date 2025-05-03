# Activity 1
# Base class - Superhero
class Superhero:
    def __init__(self, name, superpower):
        self.name = name        # Public attribute
        self.__superpower = superpower  # Private attribute (encapsulation)
    
    # Getter for the private superpower
    def get_superpower(self):
        return self.__superpower
    
    # Method to perform a fight
    def fight(self):
        print(f"{self.name} is fighting villains!")
    
    # Method to save the city
    def save_city(self):
        print(f"{self.name} is saving the city using their {self.__superpower}!")

# Derived class - Flying Superhero
class FlyingSuperhero(Superhero):
    def __init__(self, name, superpower, flight_speed):
        super().__init__(name, superpower)  # Inherit from Superhero class
        self.flight_speed = flight_speed   # Additional attribute specific to flying superheroes
    
    # Overriding the fight method for flying superhero
    def fight(self):
        print(f"{self.name} is flying while fighting villains!")
    
    # New method specific to flying superhero
    def fly(self):
        print(f"{self.name} is flying at {self.flight_speed} speed!")

# Create instances
hero1 = Superhero("Captain Marvel", "Super Strength")
hero2 = FlyingSuperhero("Superman", "Flight", "Mach 3")

# Using the methods
hero1.fight()
hero1.save_city()

hero2.fight()
hero2.save_city()
hero2.fly()

# Accessing private attribute through a getter
print(f"{hero1.name}'s superpower is {hero1.get_superpower()}")

# Activity 2
# Base class - Animal
class Animal:
    def move(self):
        print("Animal is moving in its own way.")

# Derived class - Dog
class Dog(Animal):
    def move(self):
        print("Dog is running!")

# Derived class - Bird
class Bird(Animal):
    def move(self):
        print("Bird is flying!")

# Base class - Vehicle
class Vehicle:
    def move(self):
        print("Vehicle is moving.")

# Derived class - Car
class Car(Vehicle):
    def move(self):
        print("Car is driving on the road.")

# Derived class - Plane
class Plane(Vehicle):
    def move(self):
        print("Plane is flying in the sky.")

# Create instances
animal = Animal()
dog = Dog()
bird = Bird()

car = Car()
plane = Plane()

# Polymorphism in action
for obj in [animal, dog, bird, car, plane]:
    obj.move()  # Calls the respective move() method based on the object type

