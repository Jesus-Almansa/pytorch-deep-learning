import csv
# import pandas as pd
class Item:
    # Instance level
    pay_rate = 0.8 # Pay rate after 20% discount
    all_items = []
    def __init__(self, name: str, price: float, quantity: int):
        
        # Rub validations to the received arguments
        assert price >= 0, f"Price {price} must be equal or greater than zero"
        assert quantity >= 0, f"Quantity {quantity} must be equal or greater than zero"
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all_items.append(self)
        
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

        print("Items read from CSV:")
        for item in items:
            print(item)

        
        # for item in items:            
        #     Item(
        #         name = item.get("name"),
        #         price = float(item.get("price")),
        #         quantity = int(item.get("quantity")),
        #     )
        # return pd.read_csv("./ProgramacionOrientadaObjetos/items.csv").head()
    
    @staticmethod
    def es_entero(num):
        # We will count out the floats that are point zero
        # For i.e: 0.5, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', '{self.price}', '{self.quantity}')"
    


