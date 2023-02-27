class  Pizza: 
    # Yapıcı Metot Pizza oluşturur
    def __init__(self,description,cost):
        self.description=description
        self.cost=cost
    def get_description(self):
        return self.description
    def get_cost(self):
        return self.cost
    class Classic :
        cost=5.99
        description="Classic Pizza","Pizza is a dish of Italian origin consisting of a usually round, flat base of leavened wheat-based dough topped with tomatoes, cheese, and often various other ingredients  which is then baked at a high temperature, traditionally in a wood-fired oven."
        def __init__(self):
            pass
    class Margarita :
        cost=6.99
        description="Pizza Margherita (more commonly known in English as Margherita pizza) is a typical Neapolitan pizza, made with San Marzano tomatoes, mozzarella cheese, fresh basil, salt, and extra-virgin olive oil."
    class TurkPizza :
        cost=8.99
        description="Lahmacun is also known as Turkish Pizza (or Armenian Pizza). It brings a cracker thin crust together with a flavorful (and sometimes spicy) minced meat topping."
    class Sade :
        cost=4.99
        description="In the US, a cheese pizza is the usual default option. So a plain pizza is simply another way to refer to the standard issue pie without additional toppings. If you want a pizza without cheese, you would order sauce only, no cheese."
print(Pizza.Margarita.cost)