from typing import Optional


class Item:
    def __init__(self, id_: int, name: str, price: float, stock_count: int):
        self.id = id_
        self.name = name
        self.price = price
        self.stock_count = stock_count

    def __str__(self) -> str:
        return f'ID: {self.id} | Name: {self.name} | Price: {self.price} | Count: {self.stock_count}'


class Inventory:
    def __init__(self):
        self.items = []

    def add(self, item: Item):
        self.items.append(item)

    def search(self, item_id: int) -> Optional[Item]:
        for item in self.items:
            if item.id == item_id:
                return item

        return None
