import asyncio

async def get_product():
    await asyncio.sleep(1)
    return {"id": 10, "name": "Laptop"}

async def get_stock():
    await asyncio.sleep(1.5)
    return {"available": True, "quantity": 5}

async def get_reviews():
    await asyncio.sleep(1)
    raise ValueError("Reviews service unavailable")

async def main():
    results = await asyncio.gather(
        get_product(),
        get_stock(),
        get_reviews(),
        return_exceptions=True
    )
    if isinstance(results[1], Exception) or isinstance(results[0], Exception) :
        print("failed")
        return
    elif isinstance(results[2], Exception):
        results[2]=[]
    for result in results:
        print(result)

asyncio.run(main())