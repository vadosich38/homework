import asyncio


async def every_second():
    seconds = 0

    while True:
        await asyncio.sleep(1)
        seconds += 1
        print("Прошло {} секунд".format(seconds) if seconds%3 != 0 else "")


async def every_3_sec():
    while True:
        await asyncio.sleep(3)
        print("\nПрошло еще 3 секунды")


async def main():
    task1 = asyncio.create_task(every_second())
    task2 = asyncio.create_task(every_3_sec())

    await task1
    await task2

if __name__ == "__main__":
    asyncio.run(main())
