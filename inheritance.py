#single inheritance 
"""class Animal:
    def legs(self):
        print("i have four legs")

    def fur(self):
        print("my body is covered with fur")


class dog(Animal):
    def bark(self):
        print("the dog barks")


d=dog()
d.bark()
d.legs()
d.fur()


#multilevel inheritance 
class Animal:
    def legs(self):
        print("i have two legs")

    def feather(self):
        print("my body is covered with feather")


class Hen(Animal):
    def lay(self):
        print("the hen lays eggs")

class Duck(Hen):
    def stay(self):
        print("the duck partly stays in water and in dry land")



h=Hen()
h.lay()
h.legs()
h.feather()
d=Duck()
d.stay()



#multiple inheritance 
class Mango():
    def size(self):
        print("my tree is tall")


class Passion():
    def seed(self):
        print("i have seeds")

class Fruits(Mango,Passion):
    def taste(self): 
        print("it is very sweet") 

    def use(self):
        print("useed to manufacture juices") 


f=Fruits()
f.taste()
f.use()
f.seed()
f.size()"""


#hierachical inheritance 
class Vehicles():
    def number_of_wheels(self):
        print("it has four wheels")
         
    def model(self):
        print("it is a toyota")

class Car(Vehicles):
    def type(self):
        print("it is an Audi Q7") 

    def price(self):
        print("it is worthy millions")

    def seats(self):
        print("it is a four seatter")    

class Matatu(Vehicles):
    def transport(self):
        print("it is used to transport passengers")


m=Matatu()
m.number_of_wheels()
m.model()
m.transport()
c=Car()
c.type()
c.price()
c.seats()
c.model()
c.number_of_wheels()                           



