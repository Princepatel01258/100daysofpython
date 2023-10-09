def greet(fx):
   def mfx(*args, **kwargs):
      print("Good Morning")
      fx()
      print("Thanks For Using This Function")
      return mfx


def hello():
    print("Hello World!!")
@greet(hello)()
def add(a,b):
    print(input(a) + input(b))



