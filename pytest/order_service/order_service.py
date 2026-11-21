def create_order(
    product_id,
    quantity,
    repository,
    payment_service,
    order_repository,
    email_service
):
    product = repository.get_by_id(product_id)

    if product is None:
        return False

    if product["stock"] < quantity:
        return False

    total = product["price"] * quantity

    payment_success = payment_service.charge(total)

    if not payment_success:
        return False

    order = {
        "product_id": product_id,
        "quantity": quantity,
        "total": total
    }

    order_repository.save(order)

    email_service.send_confirmation(order)

    return True