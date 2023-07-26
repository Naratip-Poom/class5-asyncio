# Wed Jul 26 14:31:47 2023 hello 0 started
# Wed Jul 26 14:31:47 2023 hello 1 started
# Wed Jul 26 14:31:47 2023 hello 2 started
# Wed Jul 26 14:31:47 2023 hello 3 started
# Wed Jul 26 14:31:47 2023 hello 4 started
# Wed Jul 26 14:31:47 2023 hello 5 started
# Wed Jul 26 14:31:47 2023 hello 6 started
# Wed Jul 26 14:31:47 2023 hello 7 started
# Wed Jul 26 14:31:47 2023 hello 8 started
# Wed Jul 26 14:31:47 2023 hello 9 started
# Wed Jul 26 14:31:51 2023 hello 0 done
# Wed Jul 26 14:31:51 2023 hello 2 done
# Wed Jul 26 14:31:51 2023 hello 5 done
# Wed Jul 26 14:31:51 2023 hello 1 done
# Wed Jul 26 14:31:51 2023 hello 4 done
# Wed Jul 26 14:31:51 2023 hello 3 done
# Wed Jul 26 14:31:51 2023 hello 6 done
# Wed Jul 26 14:31:51 2023 hello 9 done
# Wed Jul 26 14:31:51 2023 hello 7 done
# Wed Jul 26 14:31:51 2023 hello 8 done
# Time: 4.02 sec

import asyncio
import time

#เป็นฟังก์ชั่นที่ทำหน้าที่แสดงผลลัพธ์แรกเป็น Hello (จำนวนครั้ง) Started จำนวน 10 ครั้ง และรอ 4 วินาที่ตากนั้น Hello (จำนวนครั้ง) done 10 ครั้ง
async def hello(i):
    print(f"{time.ctime()} hello {i} started") #ครั้งแรก
    await asyncio.sleep(4) #รอ 4 วินาที
    print(f"{time.ctime()} hello {i} done")#ครั้งที่สอง

#ฟังกชั่นที่เริ่มรันครั้งแรกของการทำงานโปรแกรม
async def main():
    coros = [hello(i) for i in range(10)] #สร้างตัวแปรและวนลูปฟังกชั่นhello ทั้งหมด 10 ครั้ง
    await asyncio.gather(*coros)

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')#ปรินทค่าเวลาที่แสดงระยะเวลาที่โปรแกรมทำงาน