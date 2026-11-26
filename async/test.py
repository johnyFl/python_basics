import asyncio

async def get_user():
    await asyncio.sleep(3)
    return {"id": 5, "name": "Maria"}
async def get_orders():
    await asyncio.sleep(1)
    raise ValueError("Orders database unavailable")

async def main():
    task1 = asyncio.create_task(get_user())
    task2 = asyncio.create_task(get_orders())

    await asyncio.wait([task1, task2])

    if task1.exception() is not None:
        print(f"Error retrieving user: {task1.exception()}")
    else:
        print("User:", task1.result())

    if task2.exception() is not None:
        print(f"Error retrieving orders: {task2.exception()}")
    else:
        print("Orders:", task2.result())
asyncio.run(main())