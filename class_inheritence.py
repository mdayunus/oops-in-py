class Programming(object):
    raise_by = 1.20
    def __init__(self, prog_lang, pay):
        self.prog_lang = prog_lang
        self.pay = float(pay)

    def inc(self):
        self.pay = self.pay * self.raise_by



class Employee(object):
    raise_by = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = last + '.' + first + '@company.com'
        self.pay = float(pay)

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def inc(self):
        self.pay = self.pay * self.raise_by


class Developer(Programming, Employee):
    # raise_by = 1.10
    
    def __init__(self, first, last, pay, prog_lang, fav_lang):
        # super().__init__(prog_lang, pay) # use this if you have single parent else use below method and use python3 in terminal
        Employee.__init__(self, first, last, pay)
        Programming.__init__(self,prog_lang, pay)
        self.fav_lang = fav_lang

        # self.prog_lang = prog_lang

    

if __name__ == '__main__':
    # emp1 = Employee('yunus', 'ansari', 6000)
    # print(emp1.fullname())
    # emp1.inc()
    # print(emp1.pay)

    dev1 = Developer('mohd', 'yunus', 7000, 'java', 'python')
    print(dev1.pay)
    dev1.inc()
    print(dev1.pay)
    print(dev1.fullname())
    print(dev1.prog_lang)
    print(dev1.fav_lang)
    print(dev1.first)
    print(isinstance(dev1, Developer))
    print(issubclass(Developer, Employee))
    print(issubclass(Developer, Programming))
    print(issubclass(Employee, Programming))

