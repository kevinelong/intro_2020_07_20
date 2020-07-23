"""

Nouns Class/Objects (IS_A, HAS_A)

Restaurant
    Menu
    Standard Pizzas
        Meat Lover, Veggie Delight, Custom
            Custom Pizza
                Topping, Cheese, Crust
        Drinks
    Order
        LineItem
            Pizza
                Choices
                    Toppings
                        Meats ...
                        Veg ...
                    Cheese Type
                    Crust Type

            Drink
                Choices (size, Flavor)
        Pickup/Delivery
        Customer
            Addresss
            Phone
        Payment
            Credit Card
        Order Time
        Ship Time
        Delivery Time

UI User/Interface (Customer Experience):
    Loop to add line items:
        "Anything Else?"
        Python input()?

Verb Methods/Functions

Adjectives Properties/Attributes

"""

from Crust import Crust


class Order:
    pass



class Topping:
    pass


class Pizza:
    def __init__(self):
        self.toppings: [Topping] = []
        self.crust: Crust = None

    def add_topping(self, topping: Topping):
        self.toppings.append(topping)

    def set_crust_type(self, crust: Crust):
        # self.recalc_cook_time()
        self.crust = crust

    def __str__(self):
        return f"PIZZA: Options - Crust: '{self.crust}' \n"


class Customer(object):
    pass


c = Customer()

p = Pizza()
p.add_topping(Topping())
p.toppings.append(Topping())

p.crust = Crust("deep")

p.crust = Crust("thin")

crust_types = [
    Crust("regular"),
    Crust("thin"),
    Crust("deep", 100)
]

selected_crust_type = 1
p.set_crust_type(crust_types[selected_crust_type])
print(p)
