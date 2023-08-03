# Wed Jul 26 14:29:32 2023 hello 1 started
# Wed Jul 26 14:29:32 2023 hello 2 started
# Wed Jul 26 14:29:36 2023 hello 1 done
# Wed Jul 26 14:29:36 2023 hello 2 done
# Time: 4.01 sec

import asyncio
import time

#เป็นฟังก์ชั่นที่ทำหน้าที่แสดงผลลัพธ์เป็น วัน เดือน ปี และเวลา และแสดงผล Hello (จำนวนครั้ง) Started และรอ 4 วินาที่จากนันแสดงผล Hello (จำนวนครั้ง) done 

async def hello(i):
    print(f"{time.ctime()} hello {i} started")
    await asyncio.sleep(4)
    print(f"{time.ctime()} hello {i} done")
# สร้างฟังก์ชั่น main 
# สร้าง task 1, task2 ให้ทำงานพร้อมกัน โดยใช้ syncio.gather จะได้ไม่ต้องใช้หลายบรรทัด
async def main():
    task1 = asyncio.create_task(hello(1)) #return immediately, the task is created
    #await asyncio.sleep(3)
    task2 = asyncio.create_task(hello(2))
    await asyncio.gather(task1,task2)

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')