# Task A: Computing 0+1
# Task B: Computing 0+1
# Time:0.01
# Time:0.01
# Task A: Computing 1+2
# Task B: Computing 1+2
# Time:1.03
# Time:1.03
# Task B: Computing 3+3
# Task A: Sum = 3
# Time:2.03

# Task B: Sum = 6

# Time: 3.05 sec

import asyncio
import time
from concurrent.futures.thread import ThreadPoolExecutor

def sleep():
    print(f'Time:{time.time() - start:.2f}')
    time.sleep(1)
# asyncio สร้างฟังก์ชั่นรับค่าตัวแปร 2 ตัว เป็นชื่อ และ เลข
async def sum(name, numbers):
    # สร้างตัวแปร มาใช้ฟังก์ชั่นของ ThreadPoolExecutor
    _executor = ThreadPoolExecutor(2)
    # สร้างตัวแปรมาเก็บค่า คือ total
    total = 0
    # ทำการบวกเลข เก็บในตัวแปร total โดยวนลูปจาก ตัวแปร numbers 
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        await loop.run_in_executor(_executor, sleep)
        total += number
        #แสดงผลค่าที่ได้
    print(f'Task {name}: Sum = {total}\n')

start = time.time()
# asyncio สร้างฟังก์ชั่นมาเก็บค่า และสร้าง task ขึ้นมา แต่ยังไม่ให้รัน 
loop = asyncio.get_event_loop()
tasks =[
    loop.create_task(sum("A",[1,2])),
    loop.create_task(sum("B",[1,2,3])),
]
# ทำการรัน task และทำจนเสร็จ
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

end = time.time()
print(f'Time: {end-start:.2f} sec')
