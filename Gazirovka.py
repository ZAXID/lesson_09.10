class Soda:

    def __init__(self, ingredient):
        if isinstance (ingredient, str):
            self.ingredient = ingredient
        else:
            print('06b1HHaa razupoBka')

    def show_my_drink(self):
        if self.ingredient:
            print(f'Газировка и{self.ingredient}')
        else:
            print('Обычная газировка')
