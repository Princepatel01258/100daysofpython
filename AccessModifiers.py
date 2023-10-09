# Public Access Modifier
# class Employee:
#    def __init__(self):
#        self.name = "Harry"
#
# a = Employee()
# print(a.name)

# Private Access Modifier

# class Employee1:
#    def __init__(self):
#        self.__name = "Harry"
#
# a = Employee1()
# print(a._Employee1__name)
# print(a.__dir__())

# Protected Access Modifier

class student:
    def __init__(self):
        self.name = "Harry"

    def _funName(self):             #PROTECTED METHOD
        return  "Prince"

class Subject(student):
    pass

obj = student()
obj1 = Subject()
print(dir(obj))
