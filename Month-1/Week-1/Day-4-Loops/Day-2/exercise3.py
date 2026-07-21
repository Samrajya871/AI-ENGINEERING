item = input("Enter the food item:\n")

drink = input("Enter the drink:\n")

item_price = int(input("Enter the price of food item:\t"))

drink_price =  int(input("Enter the price of drink:\t"))

print("------Bill------")

print(f"{item}: {item_price}")

print(f"{drink}: {drink_price}")

print("tax : 13%")

#now for total price

total_price=(item_price+drink_price)*0.13+(item_price+drink_price)

print(f"Total Bill: {total_price}" )
