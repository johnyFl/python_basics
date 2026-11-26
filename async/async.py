import asyncio

async def get_user(user_id):
    await asyncio.sleep(1)
    print("User retrieved")
    return {"id": user_id, "name": "Alex"}


async def get_cart(user_id):
    await asyncio.sleep(2)
    print("Cart retrieved")
    return [{"product_id": 10, "quantity": 2}]


async def check_inventory(cart):
    await asyncio.sleep(2)
    print("Inventory checked")
    return True


async def calculate_shipping(cart):
    await asyncio.sleep(1)
    print("Shipping calculated")
    return 5.50


async def process_payment(user_id, cart):
    await asyncio.sleep(3)
    print("Payment completed")
    return {"payment_id": 501, "status": "success"}


async def create_order(user_id, cart, payment):
    await asyncio.sleep(1)
    print("Order created")
    return {"order_id": 9001}


async def send_confirmation_email(user):
    print("start Confirmation email sent")
    await asyncio.sleep(3)
    print("Confirmation email sent")


async def update_analytics(order):
    print("start Analytics updated")
    await asyncio.sleep(2)
    print("Analytics updated")

async def main():
    user_id = await get_user(1)
    cart = await get_cart(user_id["id"])

    inventory_ok, shipping_cost = await asyncio.gather(
        check_inventory(cart),
        calculate_shipping(cart)
    )

    if inventory_ok:
        processed_payment = await process_payment(user_id["id"], cart)
        order = await create_order(user_id["id"], cart, processed_payment)

        await asyncio.gather(
            send_confirmation_email(user_id),
            update_analytics(order)
        )

async def main():
    # 1. Παίρνουμε τον χρήστη
    user = await get_user(1)

    # 2. Το cart εξαρτάται από τον χρήστη
    cart = await get_cart(user["id"])

    # 3. Inventory και shipping είναι ανεξάρτητα μεταξύ τους
    inventory_ok, shipping_cost = await asyncio.gather(
        check_inventory(cart),
        calculate_shipping(cart)
    )

    # 4. Πληρωμή μόνο αν υπάρχει διαθέσιμο απόθεμα
    if not inventory_ok:
        return {"error": "Insufficient inventory"}

    payment = await process_payment(user["id"], cart)

    # 5. Η παραγγελία δημιουργείται μετά την επιτυχημένη πληρωμή
    order = await create_order(user["id"], cart, payment)

    # 6. Ξεκινάμε τις εργασίες στο παρασκήνιο χωρίς να τις περιμένουμε
    email_task = asyncio.create_task(
        send_confirmation_email(user)
    )
    analytics_task = asyncio.create_task(
        update_analytics(order)
    )
    # 7. Επιστρέφουμε αμέσως την απάντηση
    return {
        "message": "Order created successfully",
        "order_id": order["order_id"],
        "shipping_cost": shipping_cost
    }


asyncio.run(main())