class Employee:
    em_count=0
    def __init__ (self,name,salary):
        self.name=name
        self.salary=salary
        self.job='teacher'
        Employee.em_count+=1
    def printme(self):
        print('i am'+self.name+'my salary is'+str(self.salary))
kumar=Employee('kumar',35000)
kamal=Employee('kamal',30000)
print(kamal.name)
kamal.salary=50000
print(kamal.salary)
print(kumar.salary)
print(Employee.em_count)
kumar.printme()
