class Restaurant:
    def __init__(self, name: str, cuisine: str, menu: dict[str, float]):
        self.name = name
        self.cuisine = cuisine
        self.menu = menu
        self.reservations = 0

    def describe_restaurant(self):
        print(self.name)
        print(self.cuisine)
        print(self.menu)

    def reserve_table(self):
        if self.reservations > 10:
            print('No more reservations available.')

        else:
            self.reservations += 1
            print('Table has been reserved.')

    def take_order(self, items: list[str]):
        total = 0
        for item in items:
            total += self.menu[item]

        print(f'Total for order of {len(items)} items is {total}.')

