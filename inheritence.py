#inheritence

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
    
    
class Developer(Employee) :
    raise_amount=1.10
    def __init__(self, first, last, pay,lang):
        super().__init__(first, last, pay)
        self.lang=lang
class Manager(Employee):
    def __init__(self, first, last, pay,employees=None):
        
        super().__init__(first, last, pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees
            
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
        
    def remove_emp(self,emp):
        if emp  in self.employees:
            self.employees.remove(emp)
    def print_emps(self):
        for emp in self.employees:
            print('-->',emp.fullname())
        
        
        
        
        
dev_1 = Developer('corey', 'james', 6000,'python')
dev_2 = Developer('nick', 'james', 7000,'Java')

mgr_1=Manager("sue","smith",90000,[dev_1])
print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.print_emps()
