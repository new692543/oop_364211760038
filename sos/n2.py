"""
name: {krerkkeat Dummee}
ID : {038}
Gorup : {MIT212}

"""


# create class
class personal_record:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # private member (ไพเวดนำเบอร์ จะไม่เห็นข้อมูลจากภายนอก  _age)
        # getter and setter (เก็ตเตอร์และเช็ตเป็นตัวโอเบเลเตอร์เป็นตัวเชอรืวิดที่ใช้จัดการ  ไพเวดนำเบอร์)

    def get_age(self):
        return self.age

    def set_age(self, new_ger):
        self.__age = new_ger

    def introduce(self):
        return f'My name is {self.name}, I am {self._age} year old , I am in the room {self.gorup}.,'


# interface
name = input("Enter your name:")

age = 1
while age > 0:
    age = int(input("how old are you:"))
    if age >= 18:
        break
    else:
        print('age should be higher than 18 year old   อายุควรมากกว่า 18 ปีขึ้นไป')

obj = personal_record(name, age)
print(obj.introduce())

# loop
# for x in mypersonal_record:
#   print(x.introduce())