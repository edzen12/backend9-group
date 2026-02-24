from index11 import Verification


class V2(Verification):
    def __init__(self, login, password):
        super().__init__(login, password) # код приходит от родителя
        self.save()
        
    def save(self):
        with open("user.txt") as f:
            for line in f:
                stored_login = line.strip().split(":")[0]
                if stored_login == self.login:
                    raise ValueError("Такой пользователь уже есть")
        print("Успешно записал")
        super().save()


user1 = V2('Artem', 'qwerty2112') 