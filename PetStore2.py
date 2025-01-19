
#Created a list named "pets"
pets = ["Canine", "Feline", "Reptile"]

#Created an empty dictionary named "inventory"
inventory = {}

#Display a welcome header
print("Welcome to the Aggie Pet Store")

#Populating inventory with user input
for pet_type in pets:
    category_inventory = {}
    num_types = int(input(f"How many {pet_type} would you like to enter: "))

    for _ in range(num_types):

        pet_name = input(f"What is the type of {pet_type}: ")
        pet_cost = float(input(f"What is the price per {pet_name}: "))
        category_inventory[pet_name] = pet_cost
    
    inventory[pet_type] = category_inventory

#Displaying the inventory with cost and prices
print("\nWe offer the following pets")
for pet_type, pet_data in inventory.items():
    print(f"\n{pet_type} : ")
    
    for pet, cost in pet_data.items():
        print(f"{' ' * 4}{pet} at a cost of ${cost:,.2f}.")
