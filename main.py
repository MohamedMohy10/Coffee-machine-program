import os

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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def enough_resources(drink):
    """ Checks if there is enough ingredients for the requested drink
    returns True if there is suitable amount and false if not """
    for item in MENU[drink]['ingredients']:
        if resources[item] < MENU[drink]['ingredients'][item]:
            print(f"Sorry there is no enough {item} 😢")
            return False

    return True


def insert_money():
    """ Asks the user to insert money and returns the total paid amount after calculation
    where:
    quarter = 0.25 dollar $, dime = 0.1 dollar $, nickle = 0.05 dollar $, penny = 0.01 dollar $ """
    quarters = int(input('how many quarters?: ')) * 0.25
    dimes = int(input('how many dimes?: ')) * 0.1
    nickles = int(input('how many nickles?: ')) * 0.05
    pennies = int(input('how many pennies?: ')) * 0.01

    return quarters + dimes + nickles + pennies


def transactions_success(drink, pay):
    """ Checks if the user paid the required money
    if so : it returns True, calculates the change, Updates 'money' in resources with the paid money
    returns false if the paid money < the cost of the order"""
    drink_cost = MENU[drink]['cost']

    if pay < drink_cost:
        print(f"Sorry that's not enough money ({drink} = {drink_cost}$). Money refunded ☹️")
        return False

    print(f"Here is {format(pay - drink_cost, '.2f')}$ in change")
    resources["money"] += drink_cost
    return True


#==================================== program =======================================

os.system('cls')
while True:
    order = input(" What would you like ? (espresso\\latte\\cappuccino) ").lower()  # asks user for input
    if order == 'report':
        print(f"Water:{resources['water']} ml")
        print(f"Milk:{resources['milk']} ml")
        print(f"Coffee:{resources['coffee']} gm")
        print(f"Money:{resources['money']} $")
    if order == 'off':  # shut down the machine ==> get out of the program
        break
    if order in MENU.keys():  # checks if the order is one of the drinks available in the MENU
        if enough_resources(order):
            print("please insert coins.")
            paid_amount = insert_money()

            if transactions_success(order, paid_amount):
                # update_resources (Make Coffee 🥰):
                for item in MENU[order]['ingredients']:
                    resources[item] -= MENU[order]['ingredients'][item]
                print(f"Here is your {order} ☕ .. Enjoy! 🥰")

