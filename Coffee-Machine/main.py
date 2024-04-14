from data import MENU
from data import resources

coffee_machine_on = True
money_in_machine = 0
Approved_Inputs = ['espresso', 'latte', 'cappuccino', 'report', 'off']


def resource_check(drink):
    for drink_ingredient in MENU[drink]['ingredients']:
        check_resource = resources[drink_ingredient] - MENU[drink]['ingredients'][drink_ingredient]
        if check_resource < 0:
            print(f"Sorry, there is not enough {drink_ingredient}.")
            return False
        else:
            return True


def process_coins():
    coins = {
        'quarter': 0.25,
        'dime': 0.10,
        'nickel': 0.05,
        'penny': 0.01
    }

    coin_amounts = []

    print("Please insert coins.")

    for coin in coins:
        if coin == 'penny':
            amount_coins = int(input("How many pennies will you use?: "))
        else:
            amount_coins = int(input(f"How many {coin}s will you use?: "))

        coin_amounts.append(amount_coins * coins[coin])

    total = sum(coin_amounts)

    return round(total, 2)


# 1. TODO: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”

while coffee_machine_on:

    money = 0

    user_choice = input("Would you like an espresso, latte, or cappuccino?: ").lower()

    if user_choice not in Approved_Inputs:
        print(f"Sorry, {user_choice} is not on the menu. Please try again.")
    else:

        # 2. TODO: Turn off the Coffee Machine by entering “off” to the prompt.

        if user_choice == 'off':
            coffee_machine_on = False

        # 3. TODO: Print report

        elif user_choice == 'report':
            for resource in resources:
                if resource == 'coffee':
                    print(f"{resource.capitalize()}: {resources[resource]}g")
                else:
                    print(f"{resource.capitalize()}: {resources[resource]}ml")

            machine_money_print_text = "Money: ${money_total_txt: .2f}"
            print(machine_money_print_text.format(money_total_txt=money_in_machine))

        else:

            # 4. TODO: Check resources sufficient?

            enough_resources = resource_check(user_choice)

            # 5. TODO: Process coins

            if enough_resources:
                money = process_coins()
                cost = MENU[user_choice]['cost']

                # 6. TODO: Check transaction successful?

                if money >= cost:
                    change = money - cost
                    change_print_text = "You have ${change_txt: .2f} in change."
                    print(change_print_text.format(change_txt=change))
                    # 7. TODO: Make coffee.
                    print(f"Here is your {user_choice} ☕️. Enjoy!")

                    money_in_machine += MENU[user_choice]['cost']

                    for ingredient in MENU[user_choice]['ingredients']:
                        resources[ingredient] -= MENU[user_choice]['ingredients'][ingredient]

                else:
                    print("Sorry that's not enough money. Money refunded.")
