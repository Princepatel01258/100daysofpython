# x = (1,2,3)
# print(dir(x)) #THIS HELPS TO KNOW HOW MANY METHODS CAN YOU CAN USE ON YOUR LIST/TUPPLES/CLASS
# print(x.__add__)

class Person:
     def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1

p = Person("John", 30)
print(p.__dict__)

print(help(Person)) # HELP FN is used to know about your class / strings