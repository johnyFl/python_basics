import asyncio


async def search_airline_a(destination):
    await asyncio.sleep(4)
    print("Airline A completed")
    return {"airline": "A", "price": 220}


async def search_airline_b(destination):
    await asyncio.sleep(2)
    print("Airline B completed")
    return {"airline": "B", "price": 180}


async def search_airline_c(destination):
    await asyncio.sleep(3)
    print("Airline C completed")
    return {"airline": "C", "price": 200}


async def get_user(user_id):
    await asyncio.sleep(1)
    print("User retrieved")
    return {"id": user_id, "name": "Alex"}


async def save_search_history(user, results):
    await asyncio.sleep(2)
    print("Search history saved")


async def send_notification(user, cheapest_flight):
    await asyncio.sleep(3)
    print("Notification sent")

async def main():
    user = await get_user(1)

    tasks = [
        asyncio.create_task(search_airline_a("London")),
        asyncio.create_task(search_airline_b("London")),
        asyncio.create_task(search_airline_c("London"))
    ]

    results = []

    for task in asyncio.as_completed(tasks):
        result = await task

        print(
            f"Flight from {result['airline']} "
            f"costs {result['price']}"
        )

        results.append(result)

    cheapest_flight = min(
        results,
        key=lambda flight: flight["price"]
    )

    await save_search_history(user, results)

    asyncio.create_task(
        send_notification(user, cheapest_flight)
    )

    return {
        "cheapest_flight": cheapest_flight
    }


print(asyncio.run(main()))
