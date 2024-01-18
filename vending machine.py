name=input("What's your name? ").title()

menu={
    "A": {"item": "Piatos", "price": 3.50},
    "B": {"item": "M&M's", "price": 2.25},
    "C": {"item": "Skittles", "price": 3.00},
    "D": {"item": "Pepsi", "price": 4.50},
    "E": {"item": "Bottled Water", "price": 2.00},
    "F": {"item": "Orange Juice", "price": 3.50},}

print(f"\nHello {name}, Welcome to CJ's vending machine.\n")
print(f"What do you want {name}? ")
print("Please type the code for what you want to buy!")
print("Menu:")
for code, item in menu.items():
    print(f"{code}: {item['item']}")

order=input("\nCode: ").upper()

if order not in menu:
    print("I'm sorry, we don't have that here.")
else:
    price=menu[order]["price"]
    print(f"That would be AED {price}")

    while True:
        pay=float(input("Insert Money: AED "))

        if pay<price:
            print("That is not enough! Please insert more money.")
        else:
            break

    change=pay-price    
    item_name=menu[order]["item"]

    print(f"Your {item_name} has been dispensed.")
    print(f"Here is your change: AED {change}")
    print("Thank you for coming! Please comeback again soon!")
