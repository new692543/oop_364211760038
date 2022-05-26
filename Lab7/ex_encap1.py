# Encapsulation

class Student:
    def __init__(self,name,age):
      # odject attributes
      self.name = name
      self.age = age

    def display_info(self):
        print(f'Name: {self.name}\n  Age: {self.__age}')



    #create object of Student
    std = Student('Puriwat','35')
    print(std.name)
    print(std.age)
    std.display_info()
