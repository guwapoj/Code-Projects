# Ooremide Adegbola
# Comp163 section 2
# 3/17/24
# Adding POS (point of sale) to pet Store



#Function display menu for user options
def display_menu():
    print("A) Set Up Store")
    print("B) Display Pets")
    print("C) Sale Pet")
    print("D) Total Sale")
    print("E) Exit")


#Function SetUp for inventory setup for user
def SetUpStore():
    inventory = {}
    pets = ["Canine", "Feline", "Reptile"]
    for pet_type in pets:
        category_inventory = {}
        num_types = int(input(f"How many {pet_type} would you like to enter: "))

        for i in range(num_types):
            pet_name = input(f"What is the type of {pet_type}: ")
            pet_cost = float(input(f"What is the price per {pet_name}: "))
            category_inventory[pet_name] = pet_cost

            inventory[pet_type] = category_inventory
    return inventory




#Function to display inventory
def displayInventory(dictionary):
    print("We offer the following pets")

    for pet_type, pet_data in dictionary.items():
        print(f"\n{pet_type} : ")

        for pet, cost in pet_data.items():
            print(f"{' ' * 4}{pet} at a cost of ${cost:,.2f}.")
    print()


#Point of sale for user
def POS(line_items, inventory):
    
    item_sold_num = 1
    while True:
        print("What category would you like to sale :")
        i = 1
        for category in inventory:
            print(f"{i}. {category}")
            i += 1
        print(f"{i}. Exit")

        choice = int(input("What is being sold: ")) 
        if choice == 4:
            break
        categories = list(inventory.keys()) 
        user_category = categories[choice - 1] 
        print(f"What {user_category} are being sold:")
        i = 1
        pets = list(inventory[user_category])
        for pet in pets:
            print(f"{i}. {pet}")
            i += 1

        pet_choice = int(input(f"What {user_category} are being sold: "))
        user_pet = pets[pet_choice - 1]
        quantity = int(input(f"How many {user_pet} are being sold: "))
        line_items[item_sold_num] = [user_category, user_pet, inventory[user_category][user_pet], quantity]
        item_sold_num += 1
    return line_items


#Function to calculate tax after cost of pets
def calculateTax(price_before_tax):
    state_tax = 0.07
    federal_tax = 0.1
    state_tax_amount = price_before_tax * state_tax
    federal_tax_amount = price_before_tax * federal_tax
    total = price_before_tax + state_tax_amount + federal_tax_amount
    print(f"{' ':<14}State Tax {' ':<15}{'$'+str(round(state_tax_amount, 2)):<20}")
    print(f"{' ':<14}Federal Tax {' ':<13}{'$'+str(round(federal_tax_amount,2)):<20}")
    print(f"{' ':<14}Total Due {' ':<15}{'$'+str(round(total,2)):<20}")


#Function to display the reciept 
def displayReceipt(line_items):
    price_before_tax = 0
    print("Aggie Pet Store Bill of Sale")
    print("__________________________________________________")
    for key, values in line_items.items():
        subtotal = values[2] * values[3]
        price_before_tax += subtotal
        print(f"{key}. {values[0]:<10} {values[1]:<10} {'$'+str(values[2]):<6} {values[3]:<6} {'$'+str(subtotal):<6}")
    calculateTax(price_before_tax)
    print("__________________________________________________")


# Function to close the pet store
def closePetStore():
    print("Thank you for using the AggiePetStore POS")
    print("Aggie Pride!")

#Function for user inputs 
def user_input():
    inventory = {}
    line_items = {}

    print("Welcome to the Aggie Pet Store")
    while True:
        display_menu()
        
        menu_selection = input("Menu selection: ")

        if menu_selection == 'A':
            inventory = SetUpStore()

        elif menu_selection == 'B':
            displayInventory(inventory)

        elif menu_selection == "C":
            line_items = POS(line_items, inventory)

        elif menu_selection == "D":
            displayReceipt(line_items)
        elif menu_selection == 'E':
            closePetStore()
            break

        else:
            print("Invalid choice")

#To call user input functuon
if __name__ == "__main__":
    user_input()