class Car:
    wheels=4

c1 = Car()
c2 = Car()
Car.wheels = 5
print(c1.wheels, c2.wheels)