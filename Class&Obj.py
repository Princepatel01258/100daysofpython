class Person:
    name = "Harry"
    occupation = "Software Developer"
    nethworth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
b = Person()
a.name = "shubham"
a.occupation = "Accountant"

b.name = "Prince"
b.occupation = "HR"
print(a.name, a.occupation)
print(b.name, b.occupation)