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

profit = 0  # money --> مجموع کل پرداختی ها توسط مشتری ها تا به الان  --> profit is a global variable
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}


def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins:")
    total = int(input("How many quarters:")) * 0.25  # a quarter = $0.25
    total += int(input("How many dimes:")) * 0.1  # a dimes = $0.10
    total += int(input("How many nickles:")) * 0.05  # a nickles = $0.0.05
    total += int(input("How many pennies:")) * 0.01  # a penniess = $0.0.01
    return total  # dar majmoo user cheghadr payment anjam dade


def is_transaction_successful(money_recieved, drink_cost):
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)  # change is a local variable
        print(f"Here is your ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!!!")


is_on = True
while is_on:  # ta zamani ke dastgah on hast ( roshan )
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f" Water:{resources['water']} ml")
        print(f" Milk: {resources['milk']}ml")
        print(f" Coffee: {resources['coffee']}g")
        print(f" Money: {profit}")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()  # payment = kolle pardakhtie user ba tavajoh be tedad va arzesh har coin
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
