# Wed Jul 26 14:29:32 2023 hello 1 started
# Wed Jul 26 14:29:32 2023 hello 2 started
# Wed Jul 26 14:29:36 2023 hello 1 done
# Wed Jul 26 14:29:36 2023 hello 2 done
# Time: 4.01 sec

import asyncio
import time

#เป้นฟังก์ชั่นที่ทำหน้าที่แสดงผลลัพธ์แรกเป็น Hello (จำนวนครั้ง) Started จำนวน 10 ครั้ง และรอ 4 วินาที่ตากนั้น Hello (จำนวนครั้ง) done 10 ครั้ง
async def hello(i):
    print(f"{time.ctime()} hello {i} started")
    await asyncio.sleep(4)
    print(f"{time.ctime()} hello {i} done")

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