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
        
    def calculate_total_price(self) -> float:
        return self.price * self.quantity
    
    def apply_discount(self) -> float:
        return self.price * self.pay_rate
    
    def __repr__(self) -> str:
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"
    
