class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay


if __name__ == '__main__':
    emp_1 = Employee('yunus', 'mohd', 5000)
    print(emp_1.email)