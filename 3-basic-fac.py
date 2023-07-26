# Computing factorial(2), currently i=2...
# Computing factorial(3), currently i=2...
# Computing factorial(4), currently i=2...
# Computing factorial(3), currently i=3...
# Computing factorial(4), currently i=3...
# Computing factorial(4), currently i=4...
# [2, 6, 24]
# Time: 3.05 sec

import asyncio
import time

#ฟังกชั่นที่ทำการคำนวณค่า factorial ได้แก่ค่า [2,3,4]
async def factorial(n):
    f= 1 
    for i in range(2, n+1): 
        print(f"Computing factorial({n}), currently i={i}...")
        await asyncio.sleep(1) #แต่ละลูปของasyncronus จะดีเลย์ 1  วินาที ทำให้แต่ละ tasks ใช้เวลาทำงานไม่เท่ากัน
        f*= i
    return f

#บรรทัดเริ่มทำการคำนวณค่า factorial พร้อมกัน
async def main():
    L= await asyncio.gather(factorial(2), factorial(3), factorial(4))
    print(L) # [2,6,24] การแสดงผลค่านี้ต้องรอค่าทั้งหมดที่ถูกนำไปคำนวณทั้งสามตัวเลข

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')