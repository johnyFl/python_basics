import asyncio

async def search_database():
    await asyncio.sleep(3)
    return "Product found in database"

async def search_cache():
    await asyncio.sleep(1)
    return "Product found in cache"

async def main():
    tasks = {
        asyncio.create_task(search_database()),
        asyncio.create_task(search_cache())
    }

    done, pending = await asyncio.wait(
        tasks,
        return_when=asyncio.FIRST_COMPLETED
    )

    for task in done:
        print(await task)

    # Ακυρώνουμε όσα δεν ολοκληρώθηκαν.
    for task in pending:
        task.cancel()

    await asyncio.gather(*pending, return_exceptions=True)

asyncio.run(main())