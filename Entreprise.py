from a import salariers

class Cashier(salariers):
    def _init_(self, name='yahya', number=0, marital_status='single', address='ISGI', base_salary=0):
        
        super()._init_(name, number, marital_status, address, base_salary)

    
    def salary(self):
        return self.get_base_salary
