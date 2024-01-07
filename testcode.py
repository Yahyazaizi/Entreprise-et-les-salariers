from  a   import salariers
from Entreprise import Cashier
from b1 import Manager
from c import vendeurs

#
p1 = Manager( )
p2 = Manager("Zouhir", 345, 'single', "socoma", 20000, 2000)  
v1 = vendeurs("yahya", 345, 'single', "socoma", 10000, 15) 
v2 = vendeurs("Ahmed", 345, 'single', "socoma", 10000, 15) 
c1 = Cashier()  
c2 = Cashier("yousfe", 345, 'single', "socoma", 5000, )  


print(p1)
print(v2)
print(c1)


print("Salary:", p2.salary())
print("Salary:", v2.salary(13))
print("Salary:", c2.salary())


print(p1 == p2)
print(v1 == v2)
print(c1 == c2 )