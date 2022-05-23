"""
OOP Exercise Chapter 6

1. จงเขียนโปรแกรมภาษาไพธอนเพื่อสร้างคลาสพาหนะชื่อ Vehicle ที่ประกอบไปด้วยคุณลักษณะ (attributes) คือ 
ยี่ห้อรถ (brand) 
รุ่นรถ (model)
สีรถ (color)
ความรเร็วสูงสุด (max speed)
ราคา (price)

2.จากข้อที่ 1 เขียนโปรแกรมเพื่อสร้างวัตถุ (object) จากคลาส Vehicle โดยรับข้อมูลจากผู้ใช้ตามคุณลักษณะ (attributes)ของคลาส
จากนั้นแสดงข้อมูลทางหน้าจอภาพ

"""



car_stors = []
num = int(input('คุณมีรถกี่คัน? :'))


for x in range(num):
    brand = input('ยี่ห้อรถ:')
    model = input('รุ่นรถ:')
    color = input('สีรถ:')
    max_speed = input('ความรเร็วสูงสุด:')
    price = float(input('ราคา: '))


    b = car (brand, model, color, max_speed,price)
    car_stors.append(b)

    def display_car(car):
        for x in car:
            x.car_detail()


    display_car(car_stors)


