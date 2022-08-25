class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def info (self):
        return f'Student: {self.name}, {self.grade}'

    def isApproved(self):
        if self.grade >= 7:
            return f'{self.name} got a {self.grade}. This means the student is approved'
        else:
            return f'{self.name} got a {self.grade}. This means the student is not approved'


john = Student('John', 8)
print(john.info())
print(john.isApproved())

tom = Student('Tom', 6)
print(tom.info())
print(tom.isApproved())


