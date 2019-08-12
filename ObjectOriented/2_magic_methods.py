# dunder = double underscore methods; special purposes


class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):  # representation of object; usually for developer
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):  # readable representation of the object; usually for user
        return "{} - {}".format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee("Thomas", "Tank", 50000)
emp_2 = Employee("Big", "Bird", 60000)

# print(emp_1)

# print(repr(emp_1))
# print(str(emp_1))

# print(emp_1 + emp_2)
print(len(emp_1))
