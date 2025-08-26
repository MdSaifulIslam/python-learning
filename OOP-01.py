# Class and Object
class Product:
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price

    def display(self):
        return f"{self.name} ${self.price}"


p1 = Product(101, "Laptop", 1200)
p2 = Product(102, "Headphone", 150)
print(f"{p1.display()} and {p2.display()}")


# Methods (Instance/Class/Static)


class MathUtils:
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return MathUtils.pi * self.radius * self.radius

    @classmethod
    def changePI(cls, newPI):
        cls.pi = newPI

    @staticmethod
    def add(a, b):
        return a + b


c1 = MathUtils(4)
print(c1.area())
print(c1.add)
print(MathUtils.add)
c1.changePI(3)
print(c1.area())

#  difference between classmethod and staticmethod
# Class Method → like a company-wide policy (e.g., changing working hours) → affects all employees (objects).
# Static Method → like a general calculator tool in the office (e.g., adding two numbers)
# → doesn’t care about employees or company rules, but useful to keep it in the company’s toolbox.


# Encapsuletion
class BankAccount:
    def __init__(self, acc_no, balance, name):
        self.acc_no = acc_no
        self.__balance = balance
        self._name = name

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self.__balance


acc = BankAccount(5005, 1000000, "Saddam")
print(acc._name)  # protected printing...
print(acc._BankAccount__balance)  # # Works due to name mangling
ammount = acc._BankAccount__balance
print(ammount)
acc._BankAccount__balance = 300000
print(acc._BankAccount__balance)
print(acc.get_balance())
# print(acc.__balance) # AttributeError: 'BankAccount' object has no attribute '__balance'. Did you mean: 'get_balance'?

# Inheritance


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} {self.email}"


class Customer(User):
    def __init__(self, name, email, points):
        super().__init__(name, email)
        self.points = points
        self.name = "Sajjad"

    def __str__(self):
        return f"{super().__str__()} {self.points}"


c = Customer("Jamal", "jamal@email.com", 130)
print(c)

# Polimorphism


class Payment:
    def pay(self, amount):
        raise NotImplementedError


class CreditCard(Payment):
    def pay(self, amount):
        return f"Paid {amount} using Credit Card"


class PayPal(Payment):
    def pay(self, amount):
        return f"Paid {amount} using PayPal"


def checkout(payment: Payment, amount):
    print(payment.pay(amount))


checkout(CreditCard(), 7000)
checkout(PayPal(), 200)

# class wrapped polymorphism, but method level polymorphism like java?
# Python does not support method overloading by signature (because functions don’t have typed signatures like Java).
# If you define multiple methods with the same name, the last one wins (overwrites previous).


class MathUtils:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c


mathUtils = MathUtils()
print(mathUtils.add(1, 2, 3))  # ok
print(
    mathUtils.add(1, 2)
)  # error -> TypeError: MathUtils.add() missing 1 required positional argument: 'c'

# Abstraction
from abc import ABC, abstractmethod


class Notification:
    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending email: {message}")


class SMSNotification(Notification):
    def send(self, message):
        print(f"Sending sms: {message}")


emailNotification = EmailNotification()
emailNotification.send("Hello")


# static like variable
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1


c1 = Counter()
c2 = Counter()
c3 = Counter()

print(Counter.count)  # 3
print(c1.count)  # 3
print(c2.count)  # 3
