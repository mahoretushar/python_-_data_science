class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.price

    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.price


var_price = int(input("Enter the Price of Product 1"))
product_1 = Product(var_price)
print(product_1.price)
