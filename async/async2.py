import asyncio


async def get_user(user_id):
    await asyncio.sleep(1)
    print("User retrieved")
    return {"id": user_id, "name": "Alex"}


async def get_hotel(hotel_id):
    await asyncio.sleep(2)
    print("Hotel retrieved")
    return {"id": hotel_id, "name": "Grand Hotel"}


async def check_room_availability(hotel):
    await asyncio.sleep(2)
    print("Room availability checked")
    return True


async def calculate_booking_price(hotel):
    await asyncio.sleep(3)
    print("Booking price calculated")
    return 250.00


async def process_payment(user, price):
    await asyncio.sleep(3)
    print("Payment processed")
    return {"payment_id": 501, "status": "success"}


async def create_booking(user, hotel, payment):
    await asyncio.sleep(2)
    print("Booking created")
    return {"booking_id": 9001}


async def send_booking_email(user, booking):
    await asyncio.sleep(3)
    print("Booking email sent")


async def update_hotel_statistics(hotel, booking):
    await asyncio.sleep(2)
    print("Hotel statistics updated")

async def main():
    user = await get_user(1)

    hotel = await get_hotel(101)

    hotel_availability, booking_price = await asyncio.gather(
        check_room_availability(hotel),
        calculate_booking_price(hotel)
    )

    if not hotel_availability:
        return {"error": "No rooms available"}

    payment = await process_payment(user, booking_price)

    if payment["status"] != "success":
        return {"error": "Payment failed"}

    booking = await create_booking(user, hotel, payment)

    asyncio.create_task(send_booking_email(user, booking))
    asyncio.create_task(update_hotel_statistics(hotel, booking))

    return booking


asyncio.run(main())
        