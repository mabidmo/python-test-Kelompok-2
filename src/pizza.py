def order_pizza(n):
    if n >= 1 and n <= 10:
        order_status = "Success"
    elif n >= 11 and n <= 99:
        order_status = "Only 10 Pizza can be ordered"
    else:
        order_status = "Invalid number"
    return order_status