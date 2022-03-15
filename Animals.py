from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def b(self):
        print("hey")

class Animal:
    alive = True

    def eat(self):
        print("eating")
        return self

    def sleep(self):
        print("sleeping")
        return self
class Organism:
    def eat(self):
        print("bul bul bul")

    def breathe(self):
        print("sigh")
class Rabbit(Animal,A):
    def b(self):
        super().b()
        print("heyo")
class Fish(Animal,Organism):
    def eat(self):
        print("fish eating")
        super().eat()
        super().breathe()

def bb(a):
    a.b()
fish = Fish()
rabbit = Rabbit()
fish.eat()
rabbit.sleep().eat()
rabbit.b()
bb(rabbit)
# bb(fish)