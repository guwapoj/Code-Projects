def POS(line_items, inventory):
    
    print("What category would you like to sale :")
    print("1) Canine")
    print("2) Feline")
    print("3) Reptile")
    i = 1
    for category, pet_data in inventory.items():
        print(f"{i}. {category}")
        i += 1

    category_choice = int(input("Enter the category of pet being sold (1, 2, 3): "))
    category = list(inventory.keys())[category_choice - 1]

    print(f"\nWhat {category} are being sold:")
    i = 1
    for pet, details in inventory[category].items():
        print(f"{i}. {pet}")
        i += 1

    pet_choice = int(input(f"What {category} are being sold: "))
    pet = list(inventory[category].keys())[pet_choice - 1]

    quantity = int(input(f"How many {pet} are being sold: "))
    print(f"\nYou are selling {quantity} {pet} from the {category} category.")



def display_menu():
    print("\nAggie Pet Store Menu:")
    print("1. Add Pets")
    print("2. Display Inventory")
    print("3. Sale Pet")
    print("4. Total Sale")
    print("5. Close Pet Store")


def add_pets(inventory, pets):
    for pet_type in pets:
        category_inventory = {}
        num_types = int(input(f"How many {pet_type} would you like to enter: "))

        for i in range(num_types):
            pet_name = input(f"What is the type of {pet_type}: ")
            pet_cost = float(input(f"What is the price per {pet_name}: "))
            category_inventory[pet_name] = pet_cost

        inventory[pet_type] = category_inventory


def display_inventory(inventory):
    print("\nInventory:")
    for pet_type, pet_data in inventory.items():
        print(f"\n{pet_type} : ")

        for pet, cost in pet_data.items():
            print(f"{' ' * 4}{pet} at a cost of ${cost:,.2f}.")


def sale_pet(inventory, transaction):
    category = input("\nEnter the category of pet (Canine, Feline, Reptile): ")
    if category not in inventory:
        print("Invalid category.")
        return

    pet_type = input(f"Enter the type of {category}: ")
    if pet_type not in inventory[category]:
        print("Invalid pet type.")
        return

    quantity = int(input("Enter the quantity: "))
    if quantity > inventory[category][pet_type]:
        print("Not enough pets in inventory.")
        return

    transaction.append((pet_type, quantity))
    print("Pet sold successfully.")


def calculate_tax(line_items, state_tax_rate=0.07, federal_tax_rate=0.1):
    total_price = sum(item['price'] * item['quantity'] for item in line_items.values())
    state_tax = total_price * state_tax_rate
    federal_tax = total_price * federal_tax_rate
    total_transaction = total_price + state_tax + federal_tax
    return state_tax, federal_tax, total_transaction


def display_receipt(line_items, state_tax, federal_tax, total_transaction):
    print("\n__________________________________________________")
    print("Receipt:")
    for i, ((category, pet_type), details) in enumerate(line_items.items(), start=1):
        print(f"\nTransaction {i}:")
        print(f"Pet Category: {category}")
        print(f"Pet Type: {pet_type}")
        print(f"Pet Price: ${details['price']:.2f}")
        print(f"Quantity: {details['quantity']}")
        print(f"Line Item Total: ${details['price'] * details['quantity']:.2f}")

    print(f"\nState Tax Total: ${state_tax:.2f}")
    print(f"Federal Tax Total: ${federal_tax:.2f}")
    print(f"Total Due: ${total_transaction:.2f}")
    print("__________________________________________________")


def setup_store():
    inventory = {}
    pets = ["Canine", "Feline", "Reptile"]

    print("Welcome to the Aggie Pet Store")
    add_pets(inventory, pets)
    return inventory


def close_pet_store():
    print("Closing the Aggie Pet Store. Thank you for your visit!")


def pet_store_menu():
    inventory = {}
    transaction = {}
    while True:
        display_menu()
        choice = input("Enter your choice (1, 2, 3, 4, 5): ")
        if choice == '1':
            inventory = setup_store()
        elif choice == '2':
            display_inventory(inventory)
        elif choice == '3':
            transaction = POS(transaction, inventory)
        elif choice == '4':
            state_tax, federal_tax, total_transaction = calculate_tax(transaction)
            display_receipt(transaction, state_tax, federal_tax, total_transaction)
        elif choice == '5':
            close_pet_store()
            break
        else:
            print("Invalid choice. Please try again.")


# Main program
if __name__ == "__main__":
    pet_store_menu()
