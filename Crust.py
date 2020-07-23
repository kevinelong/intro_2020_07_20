class Crust:
    def __init__(self, name: str, additional_price=0):
        self.name = name
        self.additional_price = additional_price

    def __str__(self):
        return f"{self.name} +{(self.additional_price / 100):.2f} ' \n"

