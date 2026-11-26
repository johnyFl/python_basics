import asyncio

async def get_user():
    await asyncio.sleep(1)
    return {"id": 1, "name": "Alex"}

async def get_orders():
    await asyncio.sleep(2)
    raise ValueError("Orders database unavailable")

async def get_balance():
    await asyncio.sleep(1)
    return 250

async def main():
    user, orders, balance = await asyncio.gather(
        get_user(),
        get_orders(),
        get_balance(),
        return_exceptions=True
    )
    print("User:", user)
    print("Orders:", orders)
    print("Balance:", balance)

    results = await asyncio.gather(
        get_user(),     
        get_orders(),
        get_balance(),
        return_exceptions=True
    )   
    for result in results:
        if isinstance(result, Exception):
            print("Error:", result)
        else:
            print("Result:", result)

asyncio.run(main())