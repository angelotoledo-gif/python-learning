#Restarurant Order System
'''
def add_to_order(order, item_name, quantity, price_per_item):
    if quantity <= 0 or price_per_item <= 0:
        return False

    if item_name in order:
        order[item_name]['quantity'] += quantity
    else:
        order[item_name] = {
            'quantity': quantity,
            'price_per_item': price_per_item
        }

    return True

def remove_from_order(order, item_name):
    if item_name in order:
        del order[item_name]
        return True
    else:
        return False

def calculate_bill(order, tax_rate):
    subtotal = 0
    for item in order.values():
        subtotal += item['quantity'] * item['price_per_item']
    
    total = subtotal * (1 + tax_rate)
    return round(total, 2)

if __name__ == "__main__":
    order = {}

    print(add_to_order(order, "Burger", 2, 8.99))
    print(add_to_order(order, "Fries", -1, 2.99))
    print(add_to_order(order, "Drink", 2, 2.99))

    print(f"order: {order}")

    total = calculate_bill(order, 10)
    print(f"Total with 10% tax: ${total: .2f}")

    print(remove_from_order(order, "Drink"))
    print(remove_from_order(order, "Pizza"))
'''

import numpy as np
random_list = np.random.randint(50, 101, size=)

print(random_list)

