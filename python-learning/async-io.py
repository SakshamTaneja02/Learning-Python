import time, asyncio

async def func1():
    await asyncio.sleep(1)
    print("func1")
    return 1
async def func2():
    await asyncio.sleep(1)
    print("func2")
    return 2
async def func3():
    await asyncio.sleep(4)
    print("func3")
    return 3

async def main():
    # task = asyncio.create_task(func1())
    # await func2()
    # await func3()
    l = await asyncio.gather(func1(),func2(),func3())
    print(l)

asyncio.run(main())