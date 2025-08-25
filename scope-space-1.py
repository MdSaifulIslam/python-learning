# scope

x = "Global"


def outer():
    x = "Enclosing"

    def inner():
        x = "Local"
        print(x)  # Local

    inner()


outer()

counter = 0


# static type concept in python
def bump():
    global counter
    counter += 1
    if not hasattr(bump, "count_2"):
        bump.count_2 = 0  # initialize once
    bump.count_2 += 1
    return bump.count_2


print(bump())
print(bump())
print(bump())
print(counter)


# nonlocal
def make_bump():
    counter = 0

    def bump():
        nonlocal counter
        counter += 1
        return counter

    return bump


b = make_bump()
print(b())
print(b())


class Counter:
    counter = 0

    @classmethod
    def bump(cls):
        cls.counter += 1
        return cls.counter


print(Counter.bump())
print(Counter.bump())


# 3) Enclosing (nonlocal) scope and nonlocal
def make_accumulator():
    total = 0

    def add(n: int) -> int:
        nonlocal total
        total += n
        return total

    return add


acc = make_accumulator()
print(acc(5))
print(f"total is : {acc(10)}")


class Accumulator:
    def __init__(self):
        self.total = 0

    def add(self, n: int) -> int:
        self.total += n
        return self.total


acc = Accumulator()
print(acc.add(55))
print(acc.add(55))

# LEGB
print(f"Length is : {len([1, 2, 3, 5, 4])}")
import builtins

# print(dir(builtins))

# modify LEGB
x = 0


def outer():
    y = 0

    def inner():
        global x
        nonlocal y
        x += 10
        y += 20
        print(f"x : {x} y: {y}")

    inner()


outer()


# late binding
funcs = []
for i in range(4):

    def f(i=i):
        return i

    funcs.append(f)

print([f() for f in funcs])


# function factory
def make_f(val):
    def f():
        return val

    return f


funcs = [make_f(i) for i in range(4)]
print([f() for f in funcs])

# use lambda
func = [(lambda i=i: i) for i in range(5)]
print([f() for f in func])
