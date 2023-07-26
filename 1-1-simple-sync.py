#1-1 simple-sync.py

#ผลที่ได้จากการรัน
# Task A: Compi=uting 0+1
# Time: 0.00
# Task A: Compi=uting 1+2
# Time: 1.00
# Task A: Sum = 3

# Task B: Compi=uting 0+1
# Time: 2.01
# Task B: Compi=uting 1+2
# Time: 3.02
# Task B: Compi=uting 3+3
# Time: 4.02
# Task B: Sum = 6

# Time 5.03 sec
import time

#ฟังก์ชั้่นที่ใช้ในการแสดงค่า ระยะเวลาที่โปรแกรมใช้ในการคำนวณว่าการบวกค่าแต่ละครั้งใช้เวลากี่วินาที
def sleep():
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1)

#ฟังก์ชั่นที่นำค่าที่อยูในlist ของA และ B มาบวกกัน
def sum(name, numbers):
    total = 0 #เริ่มต้นผลบวกที่ค่าสูง
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        sleep()
        total += number
    #แสดงผลลัพธ์จากการคำนวณตามฟังก์ชั่นด้านบน
    print(f'Task {name}: Sum = {total}\n')

#สรา้งตัวแปรเก็บค่าเวลา
start = time.time()

#สร้างตัวแปร tasks ในการเก็บข้อมูลเป็น List เพื่อนำมาใช้ในการคำนวณ
tasks = [
    sum("A", [1, 2]),
    sum("B", [1,2,3]),
]
end = time.time()
print(f'Time {end-start:.2f} sec')#นำค่า endtine - starttime จะได้ค่าเวลาที่โปรแกรมใช้ในการทำงาน

