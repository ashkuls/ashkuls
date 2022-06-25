''' Munch! App MVP
V0.1
By Ash
The purpose of Munch! is to prodice a dinner menu from favorite dishes
and produce a shopping list of ingredients if required.

'''


#---------Imports---------

from random import choice

#---------A. Functions---------

#A1. Choose dishes

def chooseDishes(days):
    while len(myMenu) < int(days):
       chosenDish = choice(foodWeLike) 
       if chosenDish not in myMenu:
           myMenu.append(chosenDish)
    print("Done! Here's your menu...")
    print()
    for dish in myMenu:
        print(dish)
    print()
    print("Out of all these dishes, my favorite has to be..." + choice(myMenu) + "!")
    print()

#A2. Build shopping list function

def buildShoppingList():
    myShoppingList = []
    if "Pizza" in myMenu:
        myShoppingList.append(pizza)
    if "Rajma" in myMenu:
        myShoppingList.append(rajma)
    if "Fish and Chips" in myMenu:
        myShoppingList.append(fishAndChips)
    if "Butter Chicken" in myMenu:
        myShoppingList.append(butterChicken)
    if "Vegetarian Kofta" in myMenu:
        myShoppingList.append(vegetarianKofta)
    if "Omelette" in myMenu:
        myShoppingList.append(omelette)
    if "Chicken Biryani" in myMenu:
        myShoppingList.append(chickenBiryani)
    print()
    for dish in myShoppingList:
        for ing in dish:
            print(ing)
            print()
    print("Have a good week!")
            
    
    





#---------B. Lists---------

foodWeLike = ["Pizza", "Rajma", "Fish and Chips", "Butter Chicken", "Vegetarian Kofta", "Omelette", "Chicken Biryani"]


myMenu = []


pizza = ["Frozen Pizza Base", "Tomato and Basil Sauce", "Mozzarella"]
rajma = ["Kidney Beans", "Onions", "Rajma Paste Base"]
fishAndChips = ["Potato", "All-Purpose Flour", "Baking Powder", "Salt", "Black Pepper", "Milk", "Egg", "Oil"]
butterChicken = ["Oil", "Onion", "Garlic", "Garam Masala", "Paprika", "Salt", "Canned Diced Tomatoes", "Butter"]
vegetarianKofta = ["Frozen Koftas", "Heavy Cream", "Kofta Paste Base"]
omelette = ["Eggs", "Sunflower Oil", "Butter", "Coriander", "Onion"]
chickenBiryani = ["Chicken", "Basmati Rice", "Ghee", "Onions", "Ground Spices", "Garlic", "Ginger"]





#1.) How many days to plan?

print("Hello, I'm Munchie! I'll help you to plan your dinner menu...")

answer = input("How many days would you like me to plan?")

print("Okay! I'm going to plan" + answer + " dinner(s) from your favourite meal list!")


#2.) Choose dishes.


chooseDishes(answer)


#3.) Build shopping list?

answer = input("Would you like a shopping list for this menu?" )

if answer == 'y':
    buildShoppingList()
    

else:
    print()
   print("Okay! Bye for now:)")


