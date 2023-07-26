#ผลลัพธ์การรัน
# Task A: Computing 0+1
# Time: 0.00
# Task A: Computing 1+2
# Time: 1.01
# Task A: Sum = 3

# Task B: Computing 0+1
# Time: 2.02
# Task B: Computing 1+2
# Time: 3.03
# Task B: Computing 3+3
# Time: 4.04
# Task B: Sum = 6

# Time: 5.05 sec
import asyncio
import time
#เป็นฟังกชั่นที่ทำงานคล้ายกันกับ Asyncronus แต่ก็ไม่ใช่ asyncronus เพราะกำหนด time.sleep(1) หาต้องการเป็น Asyncronus ต้องเปลี่ยนเป้น await asyncio.sleep(1)

async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1)

async def sum(name, numbers):
    total = 0 #เริ่มต้นผลบวกที่ค่าสูง
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        await sleep()
        total += number
    print(f'Task {name}: Sum = {total}\n')

start = time.time()
 
loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(sum("A", [1, 2])),
    loop.create_task(sum("B", [1,2,3])),
]

loop.run_until_complete(asyncio.wait(tasks))
loop.close

end = time.time()
print(f'Time: {end-start:.2f} sec')