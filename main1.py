import fibo
import sys


class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        print("99999")
        return 'hello world  !!!!!!!!!!'

x = MyClass()
x.f()
print(x.f())

print(MyClass.i)

class GeeksClass:
    def say_hello(self):
        print('Hello')

# Creating an object of GeeksClass
geeks_object = GeeksClass()

# Calling the say_hello method
geeks_object.say_hello()


year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')

fibo.fib(10)

fibo.fib(1000)

print("fibo.__name__ = " + fibo.__name__)

#print(dir(sys))

print("__name__ in main1.py = " + __name__)



