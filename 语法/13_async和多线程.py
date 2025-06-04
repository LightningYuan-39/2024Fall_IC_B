import asyncio,time
async def task():
    print("任务开始")
    await asyncio.sleep(3)
    print("任务完成")
async def execute_with_timeout(t):
    try:
        await asyncio.wait_for(task(),timeout=t)
        print("任务及时完成")
    except asyncio.TimeoutError:
        print("Time Limit Exceeded")
asyncio.run(execute_with_timeout(2))
import threading
count=0
lock=threading.Lock()
def increment():
    global count
    lock.acquire()
    try:
        count+=1
    finally:
        lock.release()
threads=[]
for _ in range(10):
    thread=threading.Thread(target=increment)
    threads.append(thread)
    thread.start()
for _ in threads:
    _.join()
print(f"{count=}")