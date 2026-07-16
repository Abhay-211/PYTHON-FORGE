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
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount=amount
        
    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)
    
    @staticmethod
    def is_Workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True
        


emp1 = Employee('corey', 'james', 6000)
emp2 = Employee('nick', 'james', 7000)

import datetime
mydate= datetime.date(2016,6,11)
print(Employee.is_Workday(mydate))