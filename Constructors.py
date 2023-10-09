class Person:
   def __init__(self, name, occ): #CONSTRUCTOR IS DEFINED BY THIS WAY
       self.name = name
       self.occ = occ

   def info(self):
        print(f"{self.name} is a {self.occ} ")

a = Person("Harry", "Software DEV")
b = Person("Prince", "HR")


a.info()
b.info()