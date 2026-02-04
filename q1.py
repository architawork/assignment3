import asyncio
import random

async def producer(queue):
    for i in range(10):
        await asyncio.sleep(0.3)          # fetch data
        item = f"item-{i}"
        await queue.put(item)             # waits if queue is full
        print("Produced:", item)

async def consumer(queue):
    while True:
        item = await queue.get()          # waits if queue is empty
        await asyncio.sleep(0.5)          # process & save
        print("Consumed:", item)
        queue.task_done()

async def main():
    queue = asyncio.Queue(maxsize=3)      # backpressure

    # start one producer and one consumer
    p = asyncio.create_task(producer(queue))
    c = asyncio.create_task(consumer(queue))

    await p              # wait till producer finishes
    await queue.join()   # wait till all items are processed
    c.cancel()           # stop consumer

asyncio.run(main())
