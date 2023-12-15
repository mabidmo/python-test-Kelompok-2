from src.pizza import order_pizza

#partition 1
def test_order_pizza_minus_to_0():
    assert order_pizza(-2) == "Invalid number"

#partition 2
def test_order_pizza_1_to_10():
    assert order_pizza(5) == "Success"

#partition 2 with boundary min
def test_order_pizza_1_to_10_bound_min():
    assert order_pizza(1) == "Success"

#partition 2 with boundary max
def test_order_pizza_1_to_10_bound_max():
    assert order_pizza(10) == "Success"

#partition 3
def test_order_pizza_greater_than_11_to_99():
    assert order_pizza(12) == "Only 10 Pizza can be ordered"

#partition 3 with boundary min
def test_order_pizza_greater_than_11_to_99_bound_min():
    assert order_pizza(11) == "Only 10 Pizza can be ordered"

#partition 3 with boundary max
def test_order_pizza_greater_than_11_to_99_bound_max():
    assert order_pizza(99) == "Only 10 Pizza can be ordered"

#partition 4
def test_order_pizza_greater_than_99():
    assert order_pizza(102) == "Invalid number"
