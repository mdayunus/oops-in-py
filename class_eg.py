class Employee:

    raise_by = 1.04
    emp_count = 0


    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = float(pay)
        Employee.emp_count += 1

    def inc(self):
        self.pay = self.pay * self.raise_by

    @classmethod
    def from_string(cls, inp):
        first, last, pay = inp.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workingday(day):
        if day == 5 or day == 6 :
            return False
        return True


import datetime

if __name__ == '__main__':
    emp_1 = Employee('yunus', 'mohd', 5000)
    mydate = datetime.date(2016, 7, 15)
    myweekday = mydate.weekday()
    print(Employee.is_workingday(myweekday))
    emp_2 = Employee('baba', 'osama', 6000)
    print(Employee.emp_count)


