
# Check order_ingredients inside the parentheses.
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    """This returns true if ingredients are sufficient and order can be made. False if vv."""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item} for this drink.")
            is_enough = False
    return is_enough

def process_coins():
    """This will return the total from the coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickels?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True when payment is enough/accepted. False if vv."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Your change is: {change}")
        global profit
        # You call the global variable into the local area in order to use it.
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money.")
        return False
#     Return has to be the last thing in the function. If it's before print, print wouldn't be called.


is_on = True

while is_on:
    choice = input("What would you like? (Espresso/Latte/Cappucino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            is_transaction_successful(payment, drink["cost"])




