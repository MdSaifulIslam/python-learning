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
