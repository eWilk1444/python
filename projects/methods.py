

class BakeryItem:
    def __init__(self, type, price, flavor):
        self.type = type
        self.price = price
        self.flavor = flavor


item = BakeryItem("Muffin", 2.99, "Blueberry")
print(item.__dict__)

# name
print(BakeryItem.__name__)

# type()
item = BakeryItem("Pie", 5.99, "Apple")
print(type(item))

# __module__
print(BakeryItem.__module__)

# __bases__
print(BakeryItem.__bases__)

# getattr()
print(getattr(item, 'flavor'))

# isinstance()
print(isinstance(item, BakeryItem))
