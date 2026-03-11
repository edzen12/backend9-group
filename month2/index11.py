# Наследование, Множественное наследование, Полиморфизм
class Verification:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.__lenPassword()

    def __lenPassword(self):
        if len(self.password) < 8:
            raise ValueError("Слабый пароль")
    
    def save(self):
        with open('user.txt', 'a', encoding='utf-8') as file:
            file.write(f'{self.login}:{self.password}\n')
  
