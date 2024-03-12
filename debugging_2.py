# Similar to the previous question, debug the given python file from this
# link. It is an implementation of a food ordering system.
# Note: Use vscode “Run and Debug” with necessary breakpoints.
# (Hint: Negative quantity should not be allowed and non present food item
# should not be allowed to remove)


class FoodItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = {}

    def add_to_menu(self, food_item, quantity):
        if quantity > 0:
            if food_item in self.menu:
                self.menu[food_item] += quantity
            else:
                self.menu[food_item] = quantity
        else:
            print("Quantity must be greater than zero.")

    def remove_from_menu(self, food_item, quantity):
        if quantity > 0:
            if food_item in self.menu:
                if self.menu[food_item] < quantity:
                    print("Warning: Quantity is greater than in menu; Removed.")
                    del self.menu[food_item]
                elif self.menu[food_item] == quantity:
                    del self.menu[food_item]
                else:
                    self.menu[food_item] -= quantity
            else:
                print(f"{food_item.name} not found in the menu.")
        else:
            print("Quantity must be greater than zero.")

    def get_total_revenue(self):
        total_revenue = 0
        for food_item, quantity in self.menu.items():
            total_revenue += food_item.price * quantity
        return total_revenue


class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.cart = {}

    def add_to_cart(self, food_item, quantity):
        if quantity > 0:
            if food_item in self.cart:
                self.cart[food_item] += quantity
            else:
                self.cart[food_item] = quantity
        else:
            print("Quantity must be greater than zero.")

    def remove_from_cart(self, food_item, quantity):
        if quantity > 0:
            if food_item in self.cart:
                if self.cart[food_item] < quantity:
                    print("Warning: Quantity is greater than in cart; Removed.")
                    del self.menu[food_item]
                elif self.cart[food_item] == quantity:
                    del self.cart[food_item]
                else:
                    self.cart[food_item] -= quantity
            else:
                print(f"{food_item.name} not found in the cart.")
        else:
            print("Quantity must be greater than zero.")


class DeliveryService:
    def __init__(self):
        self.restaurants = []

    def add_restaurant(self, restaurant):
        self.restaurants.append(restaurant)

    def find_restaurant_by_name(self, name):
        for restaurant in self.restaurants:
            if restaurant.name == name:
                return restaurant
        return None


# Test the food delivery system
restaurant1 = Restaurant("Tasty Bites")
restaurant2 = Restaurant("Spice Delight")

food_item1 = FoodItem("Burger", 8)
food_item2 = FoodItem("Pizza", 12)
food_item3 = FoodItem("Pasta", 10)

restaurant1.add_to_menu(food_item1, 10)
restaurant1.add_to_menu(food_item2, 5)

restaurant2.add_to_menu(food_item2, 8)
restaurant2.add_to_menu(food_item3, 12)

customer = Customer("Alice", "123 Main St.")
customer.add_to_cart(food_item1, 2)
customer.add_to_cart(food_item2, 3)
customer.add_to_cart(food_item3, -2)  # Already fixed for negative values

delivery_service = DeliveryService()
delivery_service.add_restaurant(restaurant1)
delivery_service.add_restaurant(restaurant2)

restaurant1.remove_from_menu(food_item2, 6)  # Bug: Fixed

restaurant2.remove_from_menu(food_item1, 1)  # Bug: Fixed

print("Total revenue for Tasty Bites:", restaurant1.get_total_revenue())
print("Total revenue for Spice Delight:", restaurant2.get_total_revenue())
