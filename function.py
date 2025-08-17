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


def loop_fun(n):
    for i in range(n + 1):
        print(str(i) + " ")


# Usage examples
obj = MyClass()
return_data = obj.method()
pprint.pprint(return_data)
loop_fun(100)
pprint.pprint(type(MyClass))
pprint.pprint(type(loop_fun))
pprint.pprint(type(outer))

pprint.pprint(
    show_args(
        1,
        23,
        4,
        {"s1": 13221, "s2": 13221, "s3": 13221, "s4": 13221, "s5": 13221},
        [33, 54, 76],
        231,
        43,
        a=2,
        b=3,
        c=5,
    )
)


# functionAL Argument 1.b Custom Higher-Order Function
def apply_operation(x, y, operation):
    return operation(x, y)


def add(x, y):
    return x + y


def mul(x, y):
    return x * y


pprint.pprint(apply_operation(3, 5, add))
pprint.pprint(apply_operation(3, 5, mul))


# 1.a Using Built-in Functions (map, filter, iterable)
def square(x):
    return x * x


numbers = [1, 2, 3, 4]
result = map(square, numbers)
pprint.pprint(list(result))

result = map(lambda x: x + 10, numbers)
pprint.pprint(list(result))


def is_even(x):
    return x % 2 == 0


result = filter(is_even, numbers)
pprint.pprint(list(result))

result = filter(lambda x: x > 2, numbers)
pprint.pprint(list(result))


# 1.c Passing Lambda Functions

result = apply_operation(5, 3, lambda a, b: a + b)
print(result)

result = apply_operation(5, 3, lambda a, b: a * b)
print(result)


# 1.d callback pattern
def notify(message, callback):
    print("Sending message:", message)
    callback()


def on_sent():
    print("Message sent")


notify("Hello", on_sent)


def process_data(data, call2):
    print("Processing:", data)
    call2(data)


process_data("my_temp_data", lambda result: print("Lambda callback:", result))

# 2 Returning single or multiple values (tuples)


def get_list():
    return [1, 2, 3, 4]


def get_dict():
    return {"x": 10, "y": 30}


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def get_point():
    return Point(10, 20)


print((get_list()))
print(get_dict())
print(get_point())
print(get_point().x)
print(get_point().y)

# 3. Local vs global variables

x = "global"


def outer():
    y = "outer"

    def inner():
        global x
        nonlocal y
        x = "x modified by inner"
        y = "y modified by inner"

    inner()
    print("y in outer : ", y)


outer()
print("x in global : ", x)

# 4. Lambda Functions
# Anonymous functions for short operations
# Example: square = lambda x: x * x

default_add = lambda x, y=10: x + y
print(default_add(3))
print(default_add(3, 5))


# Lambda inside another function


def set_multiplier(n):
    return lambda x: x * n


times3 = set_multiplier(3)
print(times3(4))

times9 = set_multiplier(9)
print(times9(4))

# 5. Nested Functions & Closures
# Functions defined inside other functions


# closue
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before call")
        result = func(*args, **kwargs)
        print("After call")
        return result

    return wrapper


@my_decorator
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")


# return inner function
def make_adder(n):
    def adder(x):
        return x + n

    return adder


add5 = make_adder(5)
print(add5(15))


# return multiple inner function
def math_ops(n):
    def add(x):
        return x + n

    def mul(x):
        return x * n

    return add, mul


add4, mul4 = math_ops(4)
print(add4(16))
print(mul4(16))
