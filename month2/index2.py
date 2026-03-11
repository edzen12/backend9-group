class Car:
    def __init__(self, brand, model, year, probeg):
        self.brand = brand
        self.model = model
        self.year = year
        self.probeg = probeg
        self.speed = 0 # скорость 
        self.is_going = False # значение едет-True, не едет-False
    
    def rename(self, newBrand, newModel):
        self.brand = newBrand
        self.model = newModel
    
    def start_car(self, startSpeed):
        self.speed = startSpeed
        self.is_going = True
    
    def stop_car(self):
        self.speed = 0
        self.is_going = False

    def info(self):
        return f"""{self.brand} {self.model}, год:{self.year}, Пробег:{self.probeg}км
        машина: {"Едет" if self.is_going else 'Не едет'} со скоростью: {self.speed}км/ч""" 
    
tico = Car('Deo', 'Tico', '2004', 300000)
tico.start_car(50) 
print(tico.info())
tico.stop_car()
print(tico.info())