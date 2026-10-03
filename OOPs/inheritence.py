class Employee:
    def __init__(self, name, _id, _salary):
        self.name = name
        self._id = _id          # Protected attribute
        self._salary = _salary  # Protected attribute

    def get_details(self):
        return f"Employee Name: {self.name}, ID: {self._id}, Salary: {self._salary}"


class Manager(Employee):
    def __init__(self, name, _id, _salary, _department):
        super().__init__(name, _id, _salary)
        self._department = _department  # Protected attribute

    def get_details(self):
        return f"Manager Name: {self.name}, ID: {self._id}, Salary: {self._salary}, Department: {self._department}"

    def manage_team(self):
        print(f"{self.name} is managing the {self._department} department.")


if __name__ == "__main__":
    emp = Employee("Alice", 101, 50000)
    print(emp.get_details())

    mgr = Manager("Bob", 102, 80000, "Sales")
    print(mgr.get_details())

    mgr.manage_team()