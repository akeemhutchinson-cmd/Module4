class Item(object):
    def __init__(self, item_name, item_price, item_quantity):
        self.name = item_name
        self.price = float(item_price)
        self.quantity = int(item_quantity)

item1 = Item("Skittles", "2.99", "20")
print(item1.name)
print(item1.price)
print(item1.quantity)

item2 = Item("Baby Goldfish", "7.99", "2")
print(item2.name)
print(item2.price)
print(item2.quantity)

print("Grand Total")
print("Total cost: ", item1.price * item1.quantity + item2.price * item2.quantity)
