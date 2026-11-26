import asyncio

async def get_supplier(name, delay):
    await asyncio.sleep(delay)
    return f"{name}: product available"

async def main():
    tasks = [
        asyncio.create_task(get_supplier("Supplier A", 3)),
        asyncio.create_task(get_supplier("Supplier B", 1)),
        asyncio.create_task(get_supplier("Supplier C", 2))
    ]

    for task in asyncio.as_completed(tasks):
        result = await task
        print(result)

asyncio.run(main())