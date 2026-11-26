import asyncio

async def get_user():
    await asyncio.sleep(3)
    return {"id": 1, "name": "Alex"}


async def get_orders():
    await asyncio.sleep(1)
    raise ValueError("Orders database unavailable")


async def get_balance():
    await asyncio.sleep(3)
    return 250

async def main():
    task1 = asyncio.create_task(get_user())
    task2 = asyncio.create_task(get_orders())
    task3 = asyncio.create_task(get_balance())

    try:
        user=await task1
    except Exception as e:
        print(f"Error retrieving user: {e}")
        user = None
    try:
        orders=await task2
    except Exception as e:
        print(f"Error retrieving orders: {e}")
        orders = None
    try:
        balance=await task3
    except Exception as e:  
        print(f"Error retrieving balance: {e}")
        balance = None

    print("User:", user)
    print("Orders:", orders)
    print("Balance:", balance)
    
    await task1
    print(task1.done())
    await asyncio.sleep(4)
    print(task1.done())

asyncio.run(main())