# 6. Decorators
# Functions that modify other functions’ behavior


# logging
def log_dec(func):
    print("decoretor log_dec call whether the calling function called or not")

    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__}() returned {result}")
        return result

    return wrapper


import time


def time_dec(func):
    print("decoretor time_dec call whether the calling function called or not")

    def wrapper(*args, **kwargs):
        print(f"{func.__name__} ...")
        start = time.time()
        print(f"starting time ... {start}")
        result = func(*args, **kwargs)
        end = time.time()
        print(
            f"{func.__name__} took {end - start:.4f} seconds and the result is: {result}"
        )
        return result

    return wrapper


@time_dec
@log_dec
def add(x, y):
    return x + y


# print(add(2, 3))

# HERE IS THE CALLING SEQUENCE
# Calling add(2, 3), you are actually calling the wrapper function from time_dec, which wraps the wrapper from log_dec.

# time_dec.wrapper is called

# Prints: wrapper ...
# Records start time
# Prints: starting time ... <timestamp>
# Inside time_dec.wrapper, it calls log_dec.wrapper

# Prints: Calling add with (2, 3) {}
# Inside log_dec.wrapper, it calls the original add function

# add(2, 3) returns 5
# log_dec.wrapper resumes

# Prints: add() returned 5
# Returns 5 to time_dec.wrapper
# time_dec.wrapper resumes

# Records end time
# Prints: wrapper took 0.0005 seconds and the result is: 5
# Returns 5
# print(add(2, 3)) prints the final result

# Prints: 5

# Example form FLUENT PYTHON BOOK

registry = []


def register(func):
    print("Running register (%s)" % func)
    registry.append(func)
    return func


@register
def f1():
    print("Running f1()")


@register
def f2():
    print("Running f2()")


def f3():
    print("Running f3()")


def main():
    print("running main()")
    print("registry -> ", registry)
    f1()
    f2()
    f3()


# main()

# 7. Function as First-Class Objects
# Passing functions as arguments, returning functions, storing in variable


# 1. Assign Function to a Variable
def greet(name):
    return f"Hello {name}"


say_hello = greet
print(f"{say_hello("Afzal")}")


# 2. Passing a Function as Argument
def squre(x):
    return x * x


def apply_func(func, numbers):
    return [func(n) for n in numbers]


# print(apply_func(squre, [1, 3, 4, 5, 7, 8]))


# 3. Returning a function
def make_multiplier(n):
    def multiplier(x):
        return x * n

    return multiplier


double = make_multiplier(2)
triple = make_multiplier(3)
# print(f"{double(5)} {triple(5)}")


# 4. Store function in DS
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


operations = {"add": add, "sub": sub, "mul": mul, "div": div}
# print(
#     f"{operations['add'](2, 3)} {operations['sub'](2, 3)} {operations['mul'](2, 3)} {operations['div'](2, 3):.4}"
# )


# 8. Type Hints
# Adding type annotations for better readability and tooling
def divide(a: int, b: int) -> float | str:
    if b == 0:
        return "Error: Division by zero"
    return a / b


# print(f"{divide(10, 2)} {divide(2.2, 5)}")


# 10. Error Handling
# Using try, except blocks inside functions
def safe_divide(a, b):
    """
    This division is safe from ZeroDivisionError error.
    The program will not crush
    """
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero"
    else:
        print(f"Division successful")
        return result
    finally:
        print(f"Your division is completed!!")


print(f"{safe_divide(2, 44)}")
print(f"{safe_divide(22, 0)}")
print(safe_divide.__doc__)
