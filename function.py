import pprint


# 1. Standard function
def greet(name):
    return f"Hello, {name}!"


# 2. Function with default argument
def power(x, y=2):
    return x**y


# 3. Function with variable arguments (*args, **kwargs)
def show_args(*args, **kwargs):
    return args, kwargs


# 4. Lambda (anonymous) function
square = lambda x: x * x


# 5. Function inside another function (nested)
def outer():
    x = 20
    y = 100
    def inner():
        return "I'm inner!"
    return inner()


# 6. Function as a class method
class MyClass:
    x = 10
    y = 20
    z = 300
    def method(self):
        return "I'm a method!" + f" Value of x is {self.x} {self.y}"


# Usage examples
obj = MyClass()
return_data = obj.method()
pprint.pprint(return_data)
