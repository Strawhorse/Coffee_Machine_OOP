from menu import MENU

# global resources to be updated
profit = 0
resources = {"water": 300, "milk": 200, "coffee": 100}

# create functions
def is_resource_sufficient(order_ingredients):
    """
    Takes order ingredients as inputs and check if the available resources are there and adjust them accordingly
    """
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_coins():
    """
    Takes in the amount of money inserted to check if it is enough to pay for the drink
    """
    print("Please insert your money.")
    total = int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.1
    total += int(input("How many nickles: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """
    takes the values of the money received from process_coins() and compares it with the cost of the drink from the
    menu;
    if not enough money, returns False, prints message and returns coins
    if enough, returns True, processes the drink and returns change where necessary
    :param money_received:
    :param drink_cost:
    :return: True, False
    """
    if money_received >=drink_cost:
        global profit
        profit += drink_cost
        change = money_received - drink_cost
        print(f"Please take your change of: ${(change):.2f}.")
        return True
    else:
        print("Sorry, that is insufficient money for the drink. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """
    Deduct the required ingredients and update the resources
    """
    for item in order_ingredients:
        resources[item] -=order_ingredients[item]
    print("Please enjoy your drink! Thank you for using the Virgil 9000 Super Automatic Coffee Machine!")


# while loop to initiate the program
is_on = True
while is_on:
    print("Welcome to the Virgil 9000 Super Automatic Coffee Machine")
    print(f"Espresso: ${MENU['espresso']['cost']:.2f}; Latte: ${MENU['latte']['cost']:.2f}; Cappuccino: "
          f"${MENU['cappuccino']['cost']:.2f}")

    choice = input("What would you like? [espresso], [latte], [cappuccino]: ").lower()

    if choice == 'off':
        print("Turning the machine off now.")
        is_on = False
    elif choice == 'report':
        print(f"Money: ${profit:.2f};\nWater: {resources['water']}ml;\nMilk: {resources['milk']}ml;\nCoffee:"
              f" {resources['coffee']}g.")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])
                is_on = False