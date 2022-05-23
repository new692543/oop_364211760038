class Teacher:
    def __init__(self,name):
        self.name = name

        def introduce(self):
            print(f'My name is {self.name}, I am Teacher.')

class Student:
    def __init__(self,name):
        self.name = name

        def introduce(self):
            print(f'My name is {self.name}, I am Student.')

mylist = []
t = Teacher('Puriwat Lertkrai')
s = Student('krerkkkeat dummee')

mylist.append(t)
mylist.append(s)

for x in mylist:
    if x is not null:
    x.introduce()