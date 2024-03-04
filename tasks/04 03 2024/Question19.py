#  Write program for building restaurant menu using class in Python.


class RestaurantMenu:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f"{self.name}: ₹ {self.price} - {self.description}"

class Menu:
    def __init__(self):
        self.menu_items = []

    def add_item(self, item):
        self.menu_items.append(item)

    def print_menu(self):
        print("Restaurant Menu:")
        for item in self.menu_items:
            print(item)

if __name__ == "__main__":
    menu = Menu()

    # Adding items to the menu
    menu.add_item(RestaurantMenu("Masala Puri", 127, "Puri with masala gravy and Chutney"))
    menu.add_item(RestaurantMenu("Plain Dosa", 15, "One Dosa 15rs with sambar and chutney"))
    menu.add_item(RestaurantMenu("Biriyani", 170, "Fresh Chicken biriyani with sarlas and achar"))
    menu.add_item(RestaurantMenu("icecream", 10, "Fresh icecream from amul"))

    # Printing the menu
    menu.print_menu()
