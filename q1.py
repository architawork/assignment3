import asyncio

async def producer(queue):
    for i in range(10):
        await asyncio.sleep(0.3)        
        item = f"item-{i}"
        await queue.put(item)            
        print("Produced:", item)

async def consumer(queue):
    while True:
        item = await queue.get()          
        await asyncio.sleep(0.5)         
        print("Consumed:", item)
        queue.task_done()

async def main():
    queue = asyncio.Queue(maxsize=3)    

    p = asyncio.create_task(producer(queue))
    c = asyncio.create_task(consumer(queue))

    await p              
    await queue.join()   
    c.cancel()           

asyncio.run(main())
