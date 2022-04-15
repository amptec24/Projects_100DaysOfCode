from data import MENU, resources
from images import logo


def resources_report(water_level, milk_level, coffee_level, total_takings):
    """Print out the levels of the water, milk, coffee and money"""
    return True, f"- Water: {water_level}ml\n- Milk: {milk_level}ml\n- Coffee: {coffee_level}ml\n- Money Made: £{total_takings:.2f}\n", "system"


def money_paid():
    """User will input amount of quarters, dimes, nickles and pennies and return the total amount"""
    print("Please insert coins.")
    quarters_dropped = int(input("How many quarters? ($0.25): "))
    dimes_dropped = int(input("How many dimes? ($0.10): "))
    nickles_dropped = int(input("How many nickles? ($0.05): "))
    pennies_dropped = int(input("How many pennies ($0.01): "))
    total_paid = float((quarters_dropped * 0.25) + (dimes_dropped * 0.10) + (nickles_dropped * 0.05) + (pennies_dropped * 0.01))
    return total_paid


def compare_resources(coffee_type, water_level_check, milk_level_check, coffee_level_check):
    """Compare the levels of the all the ingredients vs what is needed to make the coffee"""
    check_water = MENU[coffee_type]["ingredients"]["water"]
    check_coffee = MENU[coffee_type]["ingredients"]["coffee"]
    if coffee_type == "espresso":
        check_milk = 0
    else:
        check_milk = MENU[coffee_type]["ingredients"]["milk"]
    if water_level_check >= check_water and milk_level_check >= check_milk and coffee_level_check >= check_coffee:
        return True, "", "system"
    elif water_level_check < check_water:
        return False, "This drink is not available! Additional water is needed to make this drink.", "system"
    elif milk_level_check <= 0:
        return False, "This drink is not available! Additional water is needed to make this drink.", "system"
    elif coffee_level_check <= 0:
        return False, "This drink is not available! Additional water is needed to make this drink.", "system"



def resources_check(water_level_check, milk_level_check, coffee_level_check):
    """Check coffee machine before offering the user the options"""
    if water_level_check <= 0:
        return True, "Out of order! Please refill with water.", "ooo"
    elif milk_level_check <= 0:
        return True, "Out of order! Please refill with milk.", "ooo"
    elif coffee_level_check <= 0:
        return True, "Out of order! Please refill with coffee.", "ooo"
    else:
        return False, "All okay!", "system"


def enough_money(coffee_type, user_paid):
    price_check = MENU[coffee_type]["cost"]
    if user_paid >= price_check:
        user_change = user_paid - price_check
        return user_change, True, price_check
    else:
        return user_paid, False, price_check


def check_make(user_selection, water_available, milk_available, coffee_available):
    """Taking the currecnt level of ingredients check to see there is enough and the reduce the current selection"""
    water_needed = MENU[user_selection]["ingredients"]["water"]
    coffee_needed = MENU[user_selection]["ingredients"]["coffee"]
    if user_selection == "espresso":
        milk_needed = 0
    else:
        milk_needed = MENU[user_selection]["ingredients"]["milk"]

    if water_available >= water_needed and milk_available >= milk_needed and coffee_available >= coffee_needed:
        water_available -= water_needed
        milk_available -= milk_needed
        coffee_available -= coffee_needed
        return water_available, milk_available, coffee_available


def user_selection_check(user_selection,water_level, milk_level, coffee_level, total_takings):
    coffee_selection_formated = user_selection.title()
    if user_selection == "off":
        return False, "Good bye, machine turning off!"
    elif user_selection == "report":
        return resources_report(water_level, milk_level, coffee_level, total_takings)
    elif user_selection == "espresso" or user_selection == "latte" or user_selection == "cappuccino":
        take_payment_check = compare_resources(user_selection, water_level, milk_level, coffee_level)
        take_payment = take_payment_check[0]
        if take_payment:
            user_paid_in = money_paid()
            make_coffee = enough_money(user_selection, user_paid_in)
            if make_coffee[1]:
                ingredients_update = check_make(user_selection, water_level, milk_level, coffee_level)
                user_changes = make_coffee[0]
                total_takings += make_coffee[2]
                if user_changes > 0:
                    return True, f"\n  Enjoy your {coffee_selection_formated} it is ready!\n  Take your ${user_changes:.2f} change.\n", make_coffee, ingredients_update
                else:
                    return True, f"\n  Enjoy your {coffee_selection_formated} it is ready!\n", make_coffee, ingredients_update
            else:
                return True, f"\n  Sorry you have inserted enough money for a {coffee_selection_formated}!\n  Your ${make_coffee[0]:.2f} was refunded.\n", "system"
        else:
            print(take_payment_check[1])
            return True, f">> You can select another drink other than {coffee_selection_formated}!.\n", "system"
    else:
        return True, "\n >> Invalid selection of coffee! Please make a new selection.\n", "system"


def coffee_machine():
    print(logo)
    continue_making_coffee = True
    water_level = resources['water']
    milk_level = resources['milk']
    coffee_level = resources['coffee']
    total_takings = 0.00

    while continue_making_coffee:
        machine_startup = resources_check(water_level, milk_level, coffee_level)
        if machine_startup[0]:
            print(machine_startup[1])
            if machine_startup[2] == "ooo":
                continue_making_coffee = False
        else:
            user_selection = input("What would you like? (espresso/latte/cappuccino): ").lower()
            coffee_selection = user_selection_check(user_selection, water_level, milk_level, coffee_level, total_takings)
            print(coffee_selection[1])
            continue_making_coffee = coffee_selection[0]
            ##################################
            #Update the avaiable resources
            if coffee_selection[0] and coffee_selection[2] != "system":
                water_level = coffee_selection[3][0]
                milk_level = coffee_selection[3][1]
                coffee_level = coffee_selection[3][2]
                total_takings += coffee_selection[2][2]

coffee_machine()