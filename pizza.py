class Pizza:
    def __init__(self, description, cost):
        self.__description = description
        self.__cost = cost
    
    def get_description(self):
        return self.__description
    
    def get_cost(self):
        return self.__cost
class Klasik(Pizza):
    description = "Klasik Pizza: Mozzarella Peynir, Domates Sosu"
    cost = 70.0
    def __init__(self, description, cost):
        super().__init__(description, cost)
    def get_cost(self):
        return super().get_cost()
    def get_description(self):
        return super().get_description()
class Margarita(Pizza):
    description = "Margarita Pizza: Mozzarella Peyniri, Domates Sosu, Taze Feslegen"
    cost = 75.0
    def __init__(self, description, cost):
        super().__init__(description, cost)
    def get_cost(self):
        return super().get_cost()
    def get_description(self):
        return super().get_description()
class TurkPizza(Pizza):

    description = "Lahmacun: Kiyma, Sogan, Domates, Yesil Biber, Maydanoz"
    cost = 25.0
    def __init__(self, description, cost):
        super().__init__(description, cost)
    def get_cost(self):
        return super().get_cost()
    def get_description(self):
        return super().get_description()
class SadePizza(Pizza):
    description = "Sade Pizza: Mozzarella Peynir, Domates Sosu, Pepperoni, Sosis, Mantar"
    cost = 72.0
    def __init__(self, description, cost):
        super().__init__(description, cost)
    def get_cost(self):
        return super().get_cost()
    def get_description(self):
        return super().get_description()
class Decorator(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def get_description(self):
       return self.pizza.get_description() + \
         ' ' + Pizza.get_description(self)

    def get_cost(self):
       return self.component.get_cost() + \
         Pizza.get_cost(self)
class Zeytin(Decorator):
    description = "Zeytin"
    cost = 5.0
    def __init__(self, pizza):
        super().__init__(pizza)
    def get_cost(self):
        return super().get_cost()
    def get_description(self):
        return super().get_description()
class Mantar(Decorator):
    description = "Mantar"
    cost = 5.0
    def __init__(self, pizza):
        super().__init__(pizza)
    def get_cost(self):
        return super().get_cost()
    def get_description(self):
        return super().get_description()
class KeciPeyniri(Decorator):
    description = "Keci Peyniri"
    cost = 5.0
    def __init__(self, pizza):
        super().__init__(pizza)
    def get_cost(self):
        return super().get_cost()
    def get_description(self):
        return super().get_description()
class Et(Decorator):
    description = "Et"
    cost = 5.0
    def __init__(self, pizza):
        super().__init__(pizza)
    def get_cost(self):
        return super().get_cost()
    def get_description(self):
        return super().get_description()
class Sogan(Decorator):
    description = "Sogan"
    cost = 5.0
    def __init__(self, pizza):
        super().__init__(pizza)
    def get_cost(self):
        return super().get_cost()
    def get_description(self):
        return super().get_description()
class Misir(Decorator):
    description = "Misir"
    cost = 5.0
    def __init__(self, pizza):
        super().__init__(pizza)
    def get_cost(self):
        return super().get_cost()
    def get_description(self):
        return super().get_description()