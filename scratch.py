
class Price:
    def __init__(self, part_number, price):
        self.price = price
        self.part_number = part_number

    def get_price(self):
        return self.price

item_price = Price(1, 150)
print(item_price.get_price()) # prints 150; method
print(item_price.part_number) # prints 1; attribute


