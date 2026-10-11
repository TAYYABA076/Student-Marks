class ShoppingCart:
    def __init__(self):
        # Each cart has its own item collection
        self.items = {}

    def add_item(self, product, price, quantity):
        self.items[product] = {
            "price": price,
            "quantity": quantity
        }

    def calculate_total(self):
        total = 0

        for item in self.items.values():
            total += item["price"] * item["quantity"]

        return total

    def remove_item(self, product):
        if product in self.items:
            del self.items[product]


# Create two separate shopping carts
cart1 = ShoppingCart()
cart2 = ShoppingCart()

# Add different items to each cart
cart1.add_item("Laptop", 800, 1)
cart1.add_item("Mouse", 25, 2)

cart2.add_item("Keyboard", 50, 1)
cart2.add_item("Headphones", 100, 2)

# Calculate totals
print("Cart 1 Total: $", cart1.calculate_total())
print("Cart 2 Total: $", cart2.calculate_total())

# Test that carts work independently
cart1.remove_item("Mouse")

print("\nAfter removing Mouse from Cart 1:")
print("Cart 1 Total: $", cart1.calculate_total())
print("Cart 2 Total: $", cart2.calculate_total())