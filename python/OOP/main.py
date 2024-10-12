
class employe:

    number_of_employees = -1

    def __init__(self, name, age, salary, working_days):
        self.name = name
        self.age = age
        self.salary = salary
        self.working_days = working_days
        employe.number_of_employees += 1
# They are the functions which work in the background

    # it help us print instance without getting an error
    def __str__(self):
        return "name : {} , age : {}".format(self.name, self.age)

    def __repr__(self):
        return "name : {} , age : {}".format(self.salary, self.working_days)
    # it is used to add two strings together
    def __add__(self, n):
        return 

employee_1 = employe("irfan" , 22, 6500, "6")
employee_2 = employe("javed" , 38, 7200, "6")
employee_3 = employe("naseem", 28, 8500, "7")
employee_4 = employe("shoeb" , 26, 7900, "5")
employee_5 = employe("naved" , 42, 8500, "5")
print("mohd" + " bilal")
print(employee_1)
print(employee_1.__repr__())

print(" _______________________________________________________________")
print("|               |          |               |                    |")
print(f"| name : {employee_1.name}  | age : {employee_1.age} | salary : {employee_1.salary} | working days : {employee_1.working_days}   |".upper())
print(f"| name : {employee_2.name}  | age : {employee_2.age} | salary : {employee_2.salary} | working days : {employee_2.working_days}   |".upper())
print(f"| name : {employee_3.name} | age : {employee_3.age} | salary : {employee_3.salary} | working days : {employee_3.working_days}   |".upper())
print(f"| name : {employee_4.name}  | age : {employee_4.age} | salary : {employee_4.salary} | working days : {employee_4.working_days}   |".upper())
print(f"| name : {employee_5.name}  | age : {employee_5.age} | salary : {employee_5.salary} | working days : {employee_5.working_days}   |".upper())
print("|_______________|__________|_______________|____________________|")

class total(employe):
    def __init__(self, name, age, salary, working_days):
        super().__init__(name,age, salary, working_days)

    # when you use @property you don't have to use () when calling the function
    @property    
    def work(self):
        summ = employee_1.salary + employee_2.salary + employee_3.salary + employee_4.salary + employee_5.salary
        return summ
    
    # when we use (same name as the property func).setter we can set value to a instances
    # for eg: self.working_days = 28293
    @work.setter
    def work(self, name):
        s = max(name)
        self.working_days = s
        
p = [employee_1.age, employee_2.age, employee_3.age, employee_4.age, employee_5.age]
v = lambda : max(p)

state = total((employe.number_of_employees), None, None, None)

lis = [employee_1.working_days, employee_2.working_days ,employee_3.working_days, employee_4.working_days, employee_5.working_days]
state.work = lis
print(" __________________________________\n|                      |           |")
print(f"|   Total Employees :  |  : {state.name}      |".upper())
print(f"|   Maximum Age     :  |  : {v()} Yrs |".upper())
print(f"|   Total Salary    :  |  : ₹{state.work} |".upper())
print(f"|   Max Working Days:  |  : {state.working_days} Days |".upper())
print("|______________________|___________|")