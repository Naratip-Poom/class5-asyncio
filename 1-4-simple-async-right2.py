# Task A: Computing 0+1
# Time: 0.00
# Task B: Computing 0+1
# Time: 0.00
# Task A: Computing 1+2
# Time: 1.01
# Task B: Computing 1+2
# Time: 1.02
# Task A: Sum = 3

# Task B: Computing 3+3
# Time: 2.02
# Task B: Sum = 6

# Time: 3.03 sec
#โค้ดนี้เป็นการทำงานแบบอะซิงโครนัสซึ่งเป็นดารทำงานพร้อมกันทั้งหมดทำให้ความเร็วในการรันโปรแกรมเร็วขึ้น
import asyncio
import time

async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    await asyncio.sleep(1)

#ฟังก์ชั่นที่ใช้ในการบวกค่าตัวเลขตามลำดับ
async def sum(name, numbers):
    # สร้างตัวแปรมาเก็บค่า คือ total
    total = 0 #เริ่มต้นผลบวกที่ค่า 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        await sleep()#ดีเลย์1วินาที
        total += number
    print(f'Task {name}: Sum = {total}\n')
#ัสร้างฟังก์ชั่นอะซิงโครนัสที่เก็บขอมูลเป็น List โดยใช้ asyncio.gather
async def main():
    await asyncio.gather(sum("A",[1,2]), sum("B",[1,2,3]))

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')