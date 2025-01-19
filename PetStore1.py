#Ooremide Adegbola
#Comp163 section 2
#2/1/24
#Creating a Pet Store List with the elements of pets with each category

#Created a list named "pets"
pets = ["Canine", "Feline", "Reptile"]
prices = []

#Welcome message for the Pet Store
print("Welcome to the Aggie Pet Store")

#Inputs for each pet and their category
price_index = 0
price = float(input(f"What is the price per {pets[price_index]}: "))
prices.append(price)
price_index += 1

price = float(input(f"What is the price per {pets[price_index]}: "))
prices.append(price)
price_index += 1

price = float(input(f"What is the price per {pets[price_index]}: "))
prices.append(price)

#Displayed the list of pets and their prices
print("We offer the following pets:")
print(f"{pets[0]} at a cost of ${prices[0]:.2f}")
print(f"{pets[1]} at a cost of ${prices[1]:.2f}")
print(f"{pets[1]} at a cost of ${prices[2]:.2f}")
#Referenced each element of the list by their index[]