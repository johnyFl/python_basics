import asyncio

async def send_notification():
    print("Sending notification...")
    await asyncio.sleep(3)
    print("Notification sent!")

async def process_order():
    print("Processing order...")
    await asyncio.sleep(2)
    print("Order processed!")

async def main():
    notification_task = asyncio.create_task(send_notification())

    await process_order()

    # Περιμένουμε να ολοκληρωθεί και η ειδοποίηση.
    await notification_task

asyncio.run(main())