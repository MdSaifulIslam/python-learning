# 6. Decorators
# Functions that modify other functions’ behavior

# logging
def log_dec(func):
    print('decoretor log_dec call whether the calling function called or not')
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__}() returned {result}")
        return result
    return wrapper

import time

def time_dec(func):
    print('decoretor time_dec call whether the calling function called or not')
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} ...")
        start = time.time()
        print(f"starting time ... {start}")
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds and the result is: {result}")
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

main()





