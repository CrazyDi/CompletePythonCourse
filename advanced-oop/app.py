from admin import Admin
from database import Database
from abc import ABCMeta, abstractmethod


a = Admin('rolf', '1234', 3)

a.save()

print(Database.find(lambda x: x['username'] == 'rolf'))


class Salary:
    # define Salary class and associated methods here
    def __init__(self, rate):
        self.rate = rate

    def calculate(self, hours):
        return self.rate * hours


class Promotable:
    # define Promotable class and associated methods here
    def __init__(self, rate):
        self.rate = rate

    def promote(self, increase):
        self.rate = self.rate + increase


# Do NOT change the code below:
class Employee(Salary, Promotable):
    def __init__(self, rate: float):
        self.rate = rate

    def weekly_salary(self) -> float:
        return self.calculate(40)


rolf = Employee(15.0)
print(rolf.weekly_salary())
rolf.promote(5.0)
print(rolf.weekly_salary())