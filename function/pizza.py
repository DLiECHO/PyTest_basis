def make_pizza(size, *toppings):
    """概述要制作的披萨"""
    print("\nMaking a " + str(size) + 
    "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

def make_hamburger(num, *toppings):
    """概述要制作的汉堡"""
    print("\nMaking a " + str(num) + 
    "s hamburgers with the following toppings:")
    for topping in toppings:
        print("- " + topping)