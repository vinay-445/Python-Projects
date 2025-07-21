Menu = {
    "latte": {
        'ingredients': {
            'water': 200,
            'milk': 150,
            'coffee': 24
        },
        'cost': 150
    },
    "espresso": {
        'ingredients': {
            'water': 50,
            'coffee': 18
        },
        'cost': 100
    },
    "cappuccino": {
        'ingredients': {
            'water': 250,
            'milk': 100,
            'coffee': 24
        },
        'cost': 200
    }
}

profit = 0
resources = {
    'water': 500,
    'coffee': 100,
    'milk': 200
}

def check_resources(ingredients):
    for item in ingredients:
        if ingredients[item] > resources.get(item, 0):
            print(f"There is not enough {item}")
            return False
    return True

def coins():
    total = 0
    print("Please insert coins")
    coins_5 = int(input("How many 5Rs. coins: "))
    coins_10 = int(input("How many 10Rs. coins: "))
    coins_20 = int(input("How many 20Rs. coins: "))
    total = (coins_5 * 5) + (coins_10 * 10) + (coins_20 * 20)
    return total

def payment_successful(money_received, coffee_cost):
    if money_received >= coffee_cost:
        global profit
        profit += coffee_cost
        change = money_received - coffee_cost
        print(f"Here is your Rs {change} in change")
        return True
    else:
        print("Enter sufficient money, your money will be refunded")
        return False

def make_coffee(coffee_name, coffee_ingredients):
    for item in coffee_ingredients:
        resources[item] -= coffee_ingredients[item]
    print(f"Here is your {coffee_name}")

on = True
while on:
    choice = input("What would you like to have? (latte/espresso/cappuccino): ")
    if choice == 'off':
        on = False
    elif choice == 'report':
        print(f"Ingredients left are\nwater: {resources['water']}ml\ncoffee: {resources['coffee']}g\nmilk: {resources['milk']}ml\nmoney: Rs {profit}")
    else:
        coffee_type = Menu.get(choice)
        if coffee_type:
            if check_resources(coffee_type['ingredients']):
                payment = coins()
                if payment_successful(payment, coffee_type['cost']):
                    make_coffee(choice, coffee_type['ingredients'])
        else:
            print("Invalid selection. Please choose from latte, espresso, or cappuccino.")
            break
