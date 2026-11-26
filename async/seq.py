import asyncio

async def get_user(user_id):
    print("Fetching user...")
    await asyncio.sleep(1)
    return {"id": user_id, "name": "John"}

async def get_orders(user_id):
    print("Fetching orders...")
    await asyncio.sleep(2)
    return ["Order 101", "Order 102"]

async def main():
    user = await get_user(1)

    orders = await get_orders(user["id"])

    print(user)
    print(orders)

asyncio.run(main())