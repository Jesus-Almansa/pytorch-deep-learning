import csv
import pandas as pd
class Item:
    # Instance level
    pay_rate = 0.8 # Pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity: int):
        
        # Rub validations to the received arguments
        assert price >= 0, f"Price {price} must be equal or greater than zero"
        assert quantity >= 0, f"Quantity {quantity} must be equal or greater than zero"
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)
        
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        return self.price * self.pay_rate
    
    #Decorators, to change the behaviour of the method
    @classmethod
    def instantiate_from_csv(cls):
        with open('./ProgramacionOrientadaObjetos/items.csv', 'r') as f:
            df = csv.DictReader(f)
            items = list(df)

        for item in items:
            Item(
                name = item.get("name"),
                price = float(item.get("price")),
                quantity = int(item.get("quantity")),
            )
        # return pd.read_csv("./ProgramacionOrientadaObjetos/items.csv")
    
    def __repr__(self) -> str:
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"
    
Item.instantiate_from_csv()
print(Item.all)