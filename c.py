from a import salariers

class vendeurs(salariers): 

    def __init__(self, name='Saad', number=0, marital_status='single', address='ISGI', base_salary=0, commission=15):
        # Constructor method for Salesperson, calling the constructor of the base class (Employee)
        super().__init__(name, number, marital_status, address, base_salary)
        self._commission = commission
       

    # Getter method for commission attribute
    @property
    def get_commission(self):
        return self._commission

    # Setter method for commission attribute
    def set_commission(self, commission):
        self._commission = commission

    # Implementation of abstract method Salary for Salesperson
    def salary(self, sales):
        return self.get_base_salary + (self.get_commission * sales)


