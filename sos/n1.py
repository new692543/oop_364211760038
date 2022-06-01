"""
name: {krerkkeat Dummee}
ID : {038}
Gorup : {MIT212}

"""


# create class
class personal_record:
    def __init__(self, name, age, gorup):
        self.name = name
        self.age = age
        self.gorup = gorup

    def introduce(self):
        return f'My name is {self.name}, I am {self.age} year old , I am in the room {self.gorup}.,'


# create object

obj = personal_record('krerkkeat Dummee', 22, 'mit212')
print(obj.introduce())

n = input('Enter your name :')
a = input('How old are you ? :')
r = input('what room are you in :')

obj2 = personal_record(n, a, r)
print(obj2.introduce())

mypersonal_record = [obj, obj2]

# loop
for x in mypersonal_record:
    print(x.introduce())