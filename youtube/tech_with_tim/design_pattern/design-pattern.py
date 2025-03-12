# Principle : Unnecessary Nesting
# Bad
# There are extra nesting in the code.
def process_numbers(numbers):
    result = []
    for num in numbers:
        if num > 0:
            if num % 2 == 0:
                if num < 100:
                    result.append(num)
                else:
                    print("Number is greater than 100")
            else:
                print("Number is not even")
        else:
            print("Number is negative")
    return result


# Good One (Refactored by Co-pilot)
def process_numbers_new(numbers):
    result = []
    for num in numbers:
        if num <= 0:
            print("Number is negative")
            continue
        if num % 2 != 0:
            print("Number is not even")
            continue
        if num >= 100:
            print("Number is greater than 100")
            continue
        result.append(num)
    return result


# Principle 2: Meaningful Naming for variable
# Bad
def process_data(d):
    res = []
    for i in d:
        if i["tp"] == "cust" and i["act"] and i["num"] > 0:
            if "bal" in i and i["bal"] > 100:
                res.append(i)
    return res


data = [
    {"tp": "cust", "act": True, "num": 10, "bal": 200},
    {"tp": "vend", "act": True, "num": 10, "bal": 50},
    {"tp": "cust", "act": True, "num": 10, "bal": 300},
    {"tp": "vend", "act": True, "num": 10, "bal": 100},
    {"tp": "cust", "act": True, "num": 10, "bal": 150},
]
output = process_data(data)


# Good
def filter_active_customers(customers):
    valid_customers = []
    for customer in customers:
        if customer["type"] != "customer":
            continue
        if not customer["active"] or customers["purchase_count"] <= 0:
            continue
        if customer.get("balance", 0) <= 100:
            continue
        valid_customers.append(customer)
    return valid_customers


customers_list = [
    {"type": "customer", "active": True, "purchase_count": 10, "balance": 200},
    {"type": "vendor", "active": True, "purchase_count": 10, "balance": 50},
    {"type": "customer", "active": True, "purchase_count": 10, "balance": 300},
    {"type": "vendor", "active": True, "purchase_count": 10, "balance": 100},
    {"type": "customer", "active": True, "purchase_count": 10, "balance": 150},
]

valid_customers = filter_active_customers(customers_list)
print(valid_customers)


# Principle 3: Single Responsibility Principle
# Bad
def process_orders(orders, inventory):
    receipts = []

    for order in orders:
        in_stock = True
        for item, qty in order["items"].items():
            if item not in inventory or inventory[item] < qty:
                print(f"{item} is out of stock")
                in_stock = False
                break
        if not in_stock:
            continue

        for item, qty in order["items"].items():
            inventory[item] -= qty
        total_price = sum([qty * price for item, qty, price in order["items"].items()])
        receipts.append({"order_id": order["id"], "total_price": total_price})
    return receipts


# Good Code

def order_in_stock(order, inventory):
    for item, qty in order["items"].items():
        if item not in inventory or inventory[item] < qty:
            print(f"{item} is out of stock")
            return False
    return True


def deduct_inventory(order, inventory):
    for item, qty in order["items"].items():
        inventory[item] -= qty  # Actually, this should be a transaction with side effect
    # Should return a new inventory object
    return inventory


def calculate_total_price(order):
    return sum([qty * price for item, qty, price in order["items"].items()])


def process_orders_new(orders, inventory):
    receipts = []

    for order in orders:
        if not order_in_stock(order, inventory):
            continue

        deduct_inventory(order, inventory)
        total_price = calculate_total_price(order)
        receipts.append({"order_id": order["id"], "total_price": total_price})
    return receipts


# Principle 4: Magic Number
# Bad
def calculate_shipping_cost(weight, destination):
    if destination == "USA":
        cost = weight * 0.5
    elif destination == "EU":
        cost = weight * 0.8
    elif destination == "Asia":
        cost = weight * 0.7
    else:
        cost = weight * 0.9
    return cost


# Good
SHIPPING_COSTS = {
    "USA": 0.5,
    "EU": 0.8,
    "Asia": 0.7,
}


def calculate_shipping_cost_new(weight, destination):
    return weight * SHIPPING_COSTS.get(destination, 0.9)


# Principle 5: Redundant Comment
# Bad
def calculate_final_price(p, t, d, c):
    # p is the price of the product
    # t is the tax rate
    # d is the discount rate
    # c is the coupon

    # Apply discount
    p = p * (1 - d)

    # Apply Coupon
    p = p - c

    # Ensure price is positive
    p = max(0, p)

    # Apply tax
    p = p * (1 + t)

    return p


# Good
def calculate_final_price_new(price, tax_rate, discount_rate, coupon):
    price = price * (1 - discount_rate)
    price = price - coupon
    price = max(0, price)
    price = price * (1 + tax_rate)
    return price
