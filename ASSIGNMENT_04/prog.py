# List of products stored as dictionaries
products = [
    {"name": "Diary", "stock": 15},
    {"name": "Notebook", "stock": 5},
    {"name": "Pencil", "stock": 8},
    {"name": "Eraser", "stock": 20},
    {"name": "Sharpener", "stock": 3}
]

print("Products with stock less than 10:")
for product in products:
    if product["stock"] < 10:
        print(f"{product['name']} - Stock: {product['stock']}")
