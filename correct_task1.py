def calculate_average_order_value(orders):
    total = 0
    valid_order_count = 0

    for order in orders:
        if order["status"] != "cancelled":
            total += order["amount"]
            valid_order_count += 1

    if valid_order_count == 0:
        return 0

    return total / valid_order_count
