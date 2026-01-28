products = [
    {"name": "Phone", "price": 500},
    {"name": "Laptop", "price": 12},
    {"name": "Mouse", "price": 99}
]

for product in products:
    if product["price"] > 100:
        print(product["name"])
    else:
        print(f"{product['name']} is under 100")
