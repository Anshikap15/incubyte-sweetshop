class Sweet:
    def __init__(self, name: str, price: float, quantity: int = 0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, qty: int):
        if qty <= 0:
            raise ValueError("Quantity must be positive")
        self.quantity += qty

    def sell(self, qty: int) -> float:
        if qty <= 0:
            raise ValueError("Quantity must be positive")
        if qty > self.quantity:
            raise ValueError("Not enough stock available")
        self.quantity -= qty
        return qty * self.price


class SweetShop:
    def __init__(self):
        self.inventory = {}

    def add_sweet(self, sweet: Sweet):
        if sweet.name in self.inventory:
            raise ValueError("Sweet already exists")
        self.inventory[sweet.name] = sweet

    def restock_sweet(self, name: str, qty: int):
        if name not in self.inventory:
            raise KeyError("Sweet not found")
        self.inventory[name].add_stock(qty)

    def sell_sweet(self, name: str, qty: int) -> float:
        if name not in self.inventory:
            raise KeyError("Sweet not found")
        return self.inventory[name].sell(qty)

    def get_inventory(self):
        return {name: sweet.quantity for name, sweet in self.inventory.items()}
