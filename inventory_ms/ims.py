import json
import uuid
from pathlib import Path
import argparse
import os

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")

add_parser = subparsers.add_parser("add")
remove_parser = subparsers.add_parser("remove")
update_parser = subparsers.add_parser("update")
list_parser = subparsers.add_parser("list")
subparsers.add_parser("summary")

add_parser.add_argument("-n", "--name", type=str, required=True)
add_parser.add_argument("-c", "--ctgry", type=str, required=True)
add_parser.add_argument("-p", "--price", type=float, required=True)
add_parser.add_argument("-s", "--stock", type=int, required=True)

remove_parser.add_argument("-n", "--name", type=str, default=None)

update_parser.add_argument("-n", "--name", type=str, default=None)
update_parser.add_argument("-p", "--price", type=float, default=None)
update_parser.add_argument("-s", "--stock", type=int, default=None)

list_parser.add_argument("-p", "--price", action="store_true")
list_parser.add_argument("-s", "--stock", action="store_true")
list_parser.add_argument("-c", "--ctgry", type=str, default=None)

args = parser.parse_args()

DATA_FILE = "inventory.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

inventory = load_data()

if args.command == "add":
    id = uuid.uuid4()
    new_product = {
        "id" : str(id),
        "name" : args.name,
        "ctgry" : args.ctgry,
        "price" : args.price,
        "stock" : args.stock
    }
    
    inventory.append(new_product)
    save_data(inventory)
    print("The product has been added.")

if args.command == "remove":
    for item in inventory:
        if item["name"] == args.name:
            inventory.remove(item)
            break
    save_data(inventory)
    print("The product has been removed.")

if args.command == "update":
    for i in range(len(inventory)):
        if inventory[i]["name"] == args.name:
            if args.price is not None:
                inventory[i]["price"] = args.price
            if args.stock is not None:
                inventory[i]["stock"] = args.stock
    save_data(inventory)
    print("The product data has been updated.")

def print_table(products_list):
    print(f"{'Name':<20} | {'Category':<15} | {'Price':>10} | {'Stock':>8}")
    print("-" * 62)

    for item in products_list:
        print(
            f"{item['name']:<20} | {item['ctgry']:<15} | ${item['price']:>9.2f} | {item['stock']:>8}"
        )

if args.command == "list":
    if args.ctgry:
        categorized_inv = [item for item in inventory if item["ctgry"] == args.ctgry]
    else:
        categorized_inv = inventory
    if not args.stock and not args.price:
        print_table(categorized_inv)
    elif args.price:
        sorted_inventory = sorted(categorized_inv, key=lambda item: item["price"])
        print_table(sorted_inventory)
    elif args.stock:
        sorted_inventory = sorted(categorized_inv, key=lambda item: item["stock"])
        print_table(sorted_inventory)

if args.command == "summary":

    total_inventory_value = 0

    for item in inventory:
        total_inventory_value += item["price"] * item["stock"]

    most_expensive_product = max(inventory, key=lambda item: item["price"])
    lowest_stock_item = min(inventory, key=lambda item: item["stock"])

    print(f"""
  Total inventory value : ${total_inventory_value:.2f}
  Most expensive product : {most_expensive_product["name"]}   (${most_expensive_product["price"]:.2f})
  Lowest stock item : {lowest_stock_item["name"]}    ({lowest_stock_item["stock"]} unit/s)
        """)

    category_groups = {}

    for item in inventory:
        if item["ctgry"] not in category_groups:
            category_groups[item["ctgry"]] = [item]
        else:
            category_groups[item["ctgry"]].append(item)

    for category, items in category_groups.items():

        category_total_value = 0
        category_total_price = 0 

        for item in items:
            category_total_value += item["price"] * item["stock"]

            category_total_price += item["price"]

        category_average_price = category_total_price / len(items)

        print(f"  {category}: ${category_total_value:.2f}  avg price: ${category_average_price:.2f}")
