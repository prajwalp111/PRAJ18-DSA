class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        if Employee.is_valid_salary(salary):
            self.salary = salary
        else:
            print("Invalid salary")
        
    @staticmethod
    def is_valid_salary(salary):
        return isinstance(salary, (int, float)) and salary >= 0

if __name__ == "__main__":
    emp = Employee("John Doe", 50000)
    print(f"Employee Name: {emp.get_name()}")
    print(f"Employee Salary: {emp.get_salary()}")
    print("Is the salary valid?", "Yes" if Employee.is_valid_salary(emp.get_salary()) else "No")
    
    emp.set_salary(60000)
    print(f"Updated Employee Salary: {emp.get_salary()}")