# 1. Class body execution
class C:
    x = 10

    def show(self):
        # print(x)   #  NameError: no `x` in local/enclosing/global/builtin
        print(C.x)  # refer to class attribute
        print(self.x)  # via reference


c = C()
# c.show()

# 3. Class attributes vs Instance attributes
# Class attributes are shared across all instances (unless shadowed).
# Instance attributes are unique to each object.


class Counter:
    count = 0  # class attribute

    def __init__(self):
        self.value = 0  # instance attribute


c1 = Counter()
c2 = Counter()

# print(Counter.count)

# print("After increment Counter.count")
# Counter.count += 1
# print(c1.count)
# print(c2.count)

# print("After increment c1.count")
# c1.count += 15
# print(c1.count)
# print(c2.count)

# print("After update Count.count")
# print(Counter.count)
# Counter.count += 15
# print(c1.count)
# print(c2.count)

# print("After increment c1.value")
# c1.value += 10
# print(c1.value)
# print(c2.value)


# 4. Class body names and methods
class Circle:
    PI = 3.1416

    def __init__(self, r):
        self.r = r

    def area(self):
        return self.PI * self.r * self.r


circle = Circle(4)
# print(circle.area())


# more explanation about self, ClassName
class Circle:
    PI = 3.14159

    def __init__(self, r):
        self.r = r

    def area_with_class(self):
        return Circle.PI * self.r * self.r

    def area_with_self(self):
        return self.PI * self.r * self.r


c = Circle(2)

print(c.area_with_class())  # 12.56636
print(c.area_with_self())  # 12.56636

# Shadow the class attribute on this instance
c.PI = 3  # instance-level attribute

print(c.area_with_class())  # 12.56636  (still Circle.PI)
print(c.area_with_self())  # 12        (used instance's PI)

# 7) Comprehension Scope in Python
# List Comprehension Variable Isolation
x = 99
squares = [x * x for x in range(9)]
print(f" x : {x}  and squares: {squares}")  # x will remain unchanged

# Dict Comprehension with External Variable
key = "user"
mydict = {key: value for key, value in [("id", 1), ("name", "asif")]}
print(key)
print(mydict)

fields = ["id", "name", "age"]
rows = [(1, "Alice", 25), (2, "Bob", 30)]

json_recodes = [{field: value for field, value in zip(fields, row)} for row in rows]

print(json_recodes)

# important note
# in loops, the loop varibale does leak
for i in range(3):
    pass
print(i)

# 8) locals(), globals(), vars(), and del in Python
# globals()
print("i" in globals())
print(globals()["i"])

config = {"Debug": True, "API_KEY": "123"}
globals().update(config)
print(Debug, API_KEY)

globals().clear()
# print(Debug, API_KEY)  # NameError: name 'Debug' is not defined


# locals()
def demo():
    a = 10
    b = 20
    print(locals())


demo()


def process_order(order_id, amount):
    print(f"Debug : {locals()}")


process_order(42, 100.9993)

# Function default values: binding time (subtle scope pitfall)
def add_item(itam, bucket=[]):
    bucket.append(itam)
    return bucket

print(add_item("one"))
print(add_item("two")) # why it appending data?

def add_item(itam, bucket = None):
    if bucket is None:
        bucket = []
    bucket.append(itam)
    return bucket
print(add_item("one"))
print(add_item("two")) 

# use for database for safe Use
def query(sql, params=None):
    if params is None:
        params = {}
        # append new data

# Exercise
# memoization
def fibo_memoized():
    cache = {0:0, 1:1}
    def fibo(n):
        nonlocal cache
        if n not in cache:
            print("running....")
            cache[n] = fibo(n-1) + fibo(n-2)
        return cache[n]
    return fibo

fib = fibo_memoized()
print(fib(10))
print("==========")
print(fib(3)) # it will print from cache

# config
class Config:
    debug = False

def log(msg):
    if Config.debug:
        print(msg)

Config.debug = True
log("Printing...")
Config.debug = False
log("Printing...") # won't print

# safe late-binding
clicking = []

for idx in range(4):
    def handler(i = idx):
        print(f"Clicking {i}")
    clicking.append(handler)

print(f"{[f() for f in clicking]}")

# super in python


class Animal:
    def __init__(self):
        print("Initializing Animal")
        super().__init__()


class Mammal(Animal):
    def __init__(self):
        print("Initializing Mammal")
        super().__init__()


class WingedAnimal(Animal):
    def __init__(self):
        print("Initializing WingedAnimal")
        super().__init__()


class Bat(Mammal, WingedAnimal):
    def __init__(self):
        print("Initializing Bat")
        # Python's MRO determines the sequence of super() calls
        super().__init__()


# b = Bat()

# Inspect the MRO
# print("\nMethod Resolution Order (MRO):")
# print(Bat.mro())

# Method Resolution Order (MRO):
# [<class '__main__.Bat'>, <class '__main__.Mammal'>, <class '__main__.WingedAnimal'>, <class '__main__.Animal'>, <class 'object'>]
