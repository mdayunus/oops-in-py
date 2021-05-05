class Employee(object):
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None

    

if __name__ == '__main__':
    emp1 = Employee('mohd', 'yunus', 7000)
    print(emp1.email)
    emp1.fullname = 'yunus ansari'
    print(emp1.fullname)
    print(emp1.email)
    print(emp1.first)
    print(emp1.last)
    del(emp1.fullname)
    print(emp1.fullname)
    print(emp1.email)
    print(emp1.first)
    print(emp1.last)



