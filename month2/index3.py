class Purse:
    def __init__(self, valuta, name='Неизвестный'):
        if valuta not in ('USD', 'KGS','EURO', 'TENGE','RUB'):
            raise ValueError("Валюта которую вы указали, не принимается у нас")
        self.valuta = valuta
        self.name = name 
        self.money = 0.00
    
    def top_up_balance(self, howmoney): #пополнение
        self.money+=howmoney
        return self.money

    def down_up_balance(self, howmoney): #снятие денег
        if self.money - howmoney <0:
            print("Недостачно средств")
            raise ValueError("Недостачно средств")
        else:
            self.money = self.money - howmoney 
            print(f"Успешно обналичили {howmoney}, осталось: {self.money}")
            return howmoney
        
    def info(self):
        return f"{self.name}: у вас на балансе: {self.money} {self.valuta}" 

argen = Purse('RUB', 'Argen')
argen.top_up_balance(200)
argen.down_up_balance(80)
print(argen.info())
        