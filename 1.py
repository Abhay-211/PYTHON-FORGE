class Employee:
    raise_amount = 1.04
    no_of_emps=0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'
        Employee.no_of_emps +=1

    def fullname(self):
        return f"{self.first} {self.last}"

    def details(self):
        return f"Name: {self.fullname()}, Email: {self.email}, Pay: {self.pay}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp1 = Employee('corey', 'james', 6000)
emp2 = Employee('nick', 'james', 7000)


# print(emp1.pay)      # 6000
# emp1.apply_raise()
# print(emp1.pay)      # 6240
print(Employee.no_of_emps)