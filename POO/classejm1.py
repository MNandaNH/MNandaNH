# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 14:40:50 2019

@author: Juan Carlos
"""

class Employee:
   'Common base class for all employees'
   empCount = 0 #nos permite contar a los epleados
#EL CONSTUCTOR metodo deiiniciacion
   def __init__(a,name, salary): #salary necesita ser parámetro y es importante para la invocación
      a.name = name
      a.salary = salary
      Employee.empCount += 1 #ES UN CONTADOR O ACUMULADOR A DONDE VAN LOS DATOS Q VOY ingresando
      
   
   def displayCount(self):
     print ("Total Employee %d", Employee.empCount) #mostrar los datos e los empelados

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

"This would create first object of Employee class"      
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Sandra", 5000)
emp3 = Employee("Ana",8000)
emp4 = Employee("Briguitte",8000)
emp5 = Employee ('Juan',1200)
emp1.displayEmployee()
emp2.displayEmployee() #usando el pto . permite definir para poder llamar el atrbuto
emp3.displayEmployee()
emp4.displayEmployee()
emp5.displayEmployee()
print ("Total Employee %d" % Employee.empCount) #cuando se llae a la variable dirá el numero de empleados q se han ingresado
emp1.displayempCount()
