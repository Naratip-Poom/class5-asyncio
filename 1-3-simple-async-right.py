# Task A: Computing 0+1
# Time: 0.00
# Task B: Computing 0+1
# Time: 0.00
# Task A: Computing 1+2
# Time: 1.01
# Task B: Computing 1+2
# Time: 1.01
# Task A: Sum = 3

# Task B: Computing 3+3
# Time: 2.03
# Task B: Sum = 6

# Time: 3.04 sec

import asyncio
import time
# ใช้ฟังก์ชั่นของ async และใช้ฟังก์ชั่นการรอแบบ async ทำให้โปรแกรมเร็วขึ้น
async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    await asyncio.sleep(1)

async def sum(name, numbers):
    # สร้างตัวแปรมาเก็บค่า คือ total
    total = 0 #เริ่มต้นผลบวกที่ค่า 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        await sleep()
        total += number
    print(f'Task {name}: Sum = {total}\n')

start = time.time()
# asyncio สร้างฟังก์ชั่นมาเก็บค่า และสร้าง task ขึ้นมา แต่ยังไม่ให้รัน 
loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(sum("A", [1, 2])),
    loop.create_task(sum("B", [1,2,3])),
]
# ทำการรัน task และทำจนเสร็จ
loop.run_until_complete(asyncio.wait(tasks))
loop.close

end = time.time()
print(f'Time: {end-start:.2f} sec')