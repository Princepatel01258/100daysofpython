class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromStr(cls, string):
        pass


@classmethod
def fromStr(cls, string):
    return cls(string.split("-")[0], string.split("-")[1])


string = "John-12000"
e1 = Employee.fromStr(string)
