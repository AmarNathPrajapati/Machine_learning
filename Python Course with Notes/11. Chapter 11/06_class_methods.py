class Employee:
    company = "Camel"
    salary = 100
    location = "Delhi"

    def changeSalary(self, sal):
        self.salary = sal
        
    # def changeSalary(self, sal):
    #     self.__class__.salary = sal

    @classmethod
    def changeSalary(cls, sal):
        cls.salary = sal

# e = Employee()
# print(e.salary)
# e.changeSalary(455)
# print(e.salary)
# print(Employee.salary)

Amar = Employee()
print(Amar.salary)
Amar.changeSalary(200)
print(Amar.salary)
print(Employee.salary)


