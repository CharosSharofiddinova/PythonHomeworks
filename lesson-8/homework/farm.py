class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound
    
    def make_sound(self):
        print(f"{self.name} says {self.sound}!")
    
    def eat(self, food):
        print(f"{self.name} is eating {food}.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")

class Cow(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Moo")
    
    def produce_milk(self):
        print(f"{self.name} is producing milk.")

class Chicken(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Cluck")
    
    def lay_egg(self):
        print(f"{self.name} has laid an egg.")

class Sheep(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Baa")
    
    def shear(self):
        print(f"{self.name} is being sheared for wool.")

# Creating instances of animals
dora = Cow("Dora", 4)
jojo = Chicken("Jojo", 2)
miya = Sheep("Miya", 3)

# Demonstrating behaviors
dora.make_sound()
dora.eat("grass")
dora.produce_milk()

jojo.make_sound()
jojo.lay_egg()

miya.make_sound()
miya.shear()
miya.sleep()
