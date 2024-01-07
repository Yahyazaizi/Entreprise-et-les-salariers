from abc import ABCMeta, abstractmethod


class salariers(metaclass=ABCMeta):
    _count = 0

    def __init__(self, name="yahya", number=0, marital_status='single', address='ISGI', base_salary=0):
        
        self._name = name
        self._number = number
        self._marital_status = marital_status
        self._address = address
        self._base_salary = base_salary
        salariers._count += 1
        self._employee_id = salariers._count
        
    # Property getters for various attributes
    @property
    def get_name(self):
        return self._name

    @property
    def get_number(self):
        return self._number

    @property
    def get_marital_status(self):
        return self._marital_status

    @property
    def get_address(self):
        return self._address

    @classmethod
    def get_count(cls):
        return salariers._count

    @property
    def get_employee_id(self):
        return self._employee_id

   

    @property
    def get_base_salary(self):
        return self._base_salary

    # Setter methods for various attributes
    def set_name(self, name):
        self._name = name

    def set_number(self, number):
        self._number = number

    def set_marital_status(self, status):
        self._marital_status = status

    def set_address(self, address):
        self._address = address

    def set_employee_id(self, employee_id):
        self._employee_id = employee_id

    def set_base_salary(self, base_salary):
        self._base_salary = base_salary

    
    # Abstract method representing the salary calculation
    @abstractmethod
    def salary(self, sales=0):
        pass

    # Custom equality method for comparing instances
    def __eq__(self, other):
        if type(self) == type(other):
            return (self.salary == other.salary) and (self.get_employee_id == other.get_employee_id)
        else:
            return "Not the same type"
         
        

    # Custom string representation method
    def __str__(self):
        return f'Name: {self.get_name}, Number: {self.get_number}, Marital Status: {self.get_marital_status}, Address: {self.get_address}, Employee ID: {self.get_employee_id}, Base Salary: {self.get_base_salary}'
