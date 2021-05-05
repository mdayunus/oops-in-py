class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __add__(self, other):
        if isinstance(other, Employee):
            return self.pay + other.pay
        return -1

    def __str__(self): #readable respresentation of object and is meant to be display to the end user
        return self.fullname()

    def __repr__(self): #unambegious representation of object and should be use for debigging and logging and things like that
        return '{} {}'.format(self.first, self.email)




if __name__ == '__main__':
    emp1 = Employee('yunus', 'ansari', 7000)
    emp2 = Employee('arslan', 'ahmad', 4000)
    print(emp1 + 3) # + is not working on this because we are using isinsntace in code which is a really good practice
    print(emp1 + emp2)
    print(emp1)
    emp1.first = 'mohd'
    print(emp1.first)
    print(emp1.email)
    