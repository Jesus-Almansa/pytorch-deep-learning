from item import Item
class Phone(Item):
    # Instance level
    pay_rate = 0.8 # Pay rate after 20% discount
    def __init__(self, name: str, price: float, quantity: 0, broken_phones: 0):
        # Call to super function to have access to all attributes/methods
        super().__init__(name, price, quantity)

        # Rub validations to the received arguments
        assert broken_phones >= 0, f"Broken_phones {broken_phones} must be equal or greater than zero"

        # Assign to self object
        self.broken_phones = broken_phones