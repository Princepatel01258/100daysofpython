x = 10 # Global Var
# print(x)


def my_func():

    global x
    x = 4 
    y = 5  # Local Var
    print(y)

my_func()
print(x)
# print(y)