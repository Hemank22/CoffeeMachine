from main import MENU, resources

profit = 0


def is_resource_sufficient(order_ingredients):
    """Returns true if order can be made else tells if the resources are not enough"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins():
    """Returns the total calculated amount from the coins inserted"""
    print("Please insert coins. ")
    total = int(input("How many quarters?")) * 0.25
    # Quarter = 0.25 Dollar
    total += int(input("How many dimes?")) * 0.1
    total += int(input("How many nickles?")) * 0.05
    total += int(input("How many pennies?")) * 0.01
    return total


def is_transaction_successful(money_received, cost_of_drink):
    """Returns true if payment is accepted or false if money is insufficient"""
    if money_received >= cost_of_drink:
        change = round(money_received - cost_of_drink, 2)
        print(f"Here is ${change} change.")
        global profit
        profit += cost_of_drink
        return True
    else:
        print("Sorry that's not enough money. Money is refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deducts the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money:${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
