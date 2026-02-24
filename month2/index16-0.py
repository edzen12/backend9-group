# Валюта - Currency
class Currency:
    def __init__(self, value):
        self.value = value
    
    def convert_to_som(self):
        pass 

    @classmethod
    def from_som(cls, som_value):
        return som_value/cls.rate_to_som

    def print_value(self):
        print(self.value, end=" ")


class Dollar(Currency):
    rate_to_som = 87.45
    suffix = 'USD'

    def convert_to_som(self):
        som = self.value*Dollar.rate_to_som
        return som 
    
    def print_value(self):
        super().print_value()
        print(Dollar.suffix, end=' ')


class Euro(Currency):
    rate_to_som = 103.40
    suffix = 'Euro'

    def convert_to_som(self):
        som = self.value*Euro.rate_to_som
        return som 
    
    def print_value(self):
        super().print_value()
        print(Euro.suffix, end=' ')


d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
e = [Euro(5), Euro(10), Euro(50), Euro(100)]

for i in d:
    i.print_value()
    print(f"= {i.convert_to_som():.2f} Сом")

for i in e:
    i.print_value()
    print(f"= {i.convert_to_som():.2f} Сом")


som_input = float(input("Введите сумму в сомах: "))
usd_amount = Dollar.from_som(som_input)
euro_amount = Euro.from_som(som_input)
print(f"{som_input:.2f} сом = {usd_amount:.2f} USD")
print(f"{som_input:.2f} сом = {euro_amount:.2f} Euro")