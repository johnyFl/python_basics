import asyncio

async def get_user():
    await asyncio.sleep(2)
    return {"name": "John"}

async def get_products():
    await asyncio.sleep(3)
    return ["Mouse", "Keyboard"]

async def get_categories():
    await asyncio.sleep(1)
    return ["Electronics", "Accessories"]

async def main():
    user, products, categories = await asyncio.gather(
        get_user(),
        get_products(),
        get_categories()
    )

    print(user)
    print(products)
    print(categories)

asyncio.run(main())