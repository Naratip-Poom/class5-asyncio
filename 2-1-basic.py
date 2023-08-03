#ผลลัพธ์การรัน
# Wed Jul 26 14:27:44 2023 hello 1 started
# Wed Jul 26 14:27:44 2023 hello 2 started
# Wed Jul 26 14:27:48 2023 hello 1 done
# Wed Jul 26 14:27:48 2023 hello 2 done
# Time: 4.03 sec

import asyncio
import time
#เป็นฟังก์ชั่นที่ทำหน้าที่แสดงผลลัพธ์เป็น วัน เดือน ปี และเวลา และแสดงผล Hello (จำนวนครั้ง) Started และรอ 4 วินาที่จากนันแสดงผล Hello (จำนวนครั้ง) done
async def hello(i):
    print(f"{time.ctime()} hello {i} started")
    await asyncio.sleep(4)
    print(f"{time.ctime()} hello {i} done")
# สร้างฟังก์ชั่น main สร้าง task 1, task2 และ ให้ทำงานพร้อมกัน
async def main():
    task1 = asyncio.create_task(hello(1)) #return immediately, the task is created
    #await asyncio.sleep(3)
    task2 = asyncio.create_task(hello(2))
    await task1
    await task2
#run ฟังก์ชั่น main()
#จับเวลา และ print เวลา
if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')