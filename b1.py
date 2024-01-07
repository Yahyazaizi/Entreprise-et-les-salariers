from a import salariers

class Manager(salariers):
    def __init__(self, name='yahya', number=0, marital_status='single', address='ISGI', base_salary=0,  bonus=0):
        # Constructor method for Manager, calling the constructor of the base class (Employee)
        super().__init__(name, number, marital_status, address, base_salary)
        self._bonus = bonus

    # Getter method for bonus attribute
    @property
    def get_bonus(self):
        return self._bonus

    # Setter method for bonus attribute
    def set_bonus(self, bonus):
        self._bonus = bonus

    # Implementation of abstract method Salary for Manager
    def salary(self):
        return self.get_base_salary + self.get_bonus
