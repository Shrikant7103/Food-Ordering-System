# Define the menu globally
menu = {
    'Pasta': 250,
    'Pizza': 300,
    'Salad': 150
}

def display_menu():
    print("------- Menu -------")
    for item, price in menu.items():
        print(f"{item}: ₹{price}")
    print("--------------------\n")

# Greet the customer and display the menu
print("Welcome to our restaurant!")
display_menu()

order_total = 0

# Take the first order
item_1 = input("Enter the name of the item you want to order: ").title()
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item '{item_1}' has been added to your order.")
else:
    print(f"Ordered item '{item_1}' is not available.")

# Ask if the customer wants to add another item
another_item = input("Do you want to add another item? (Yes/No): ").strip().lower()
if another_item == "yes":
    item_2 = input("Enter the second item: ").title()
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item '{item_2}' has been added to your order.")
    else:
        print(f"Ordered item '{item_2}' is not available.")



another_item = input("Do you want to add another item? (Yes/No): ").strip().lower()
if another_item == "yes":
    item_3= input("Enter the second item: ").title()
    if item_3 in menu:
        order_total += menu[item_2]
        print(f"Item '{item_3}' has been added to your order.")
    else:
        print(f"Ordered item '{item_3}' is not available.")

print(f"\nThe total amount for your order is: ₹{order_total}")
