import json

products =[
    {"name": "Laptop", "price": 75000, "quantity": 5},
    {"name": "Mobile", "price": 25000, "quantity": 10},
    {"name": "Earphones", "price": 2000, "quantity": 20}
]   

with open("products.json", "w") as file:
    json.dump(products, file, indent=4)

print("JSON file created successfully!")

with open("products.json", "r") as file:
    data = json.load(file)

print("\nName\t\tPrice\t\tQuantity")

for item in data:
    print(item["name"], "\t\t", item["price"], "\t\t", item["quantity"])