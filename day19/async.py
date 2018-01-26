import asyncio


async def count_down(name):
    for i in range(10, 0, -1):
        print("{}: {}".format(name, str(i)))
        await asyncio.sleep(1)


loop = asyncio.get_event_loop()
tasks = [
    asyncio.ensure_future(count_down("A")),
    asyncio.ensure_future(count_down("B")),
    asyncio.ensure_future(count_down("C"))
]

loop.run_until_complete(asyncio.wait(tasks))
loop.close()