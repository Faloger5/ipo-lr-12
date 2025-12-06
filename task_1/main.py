#Доброва Анна
class Client:
    # Класс клиента, у которого есть имя, вес груза и статус VIP
    def __init__(self, name, cargo_weight, is_vip=False):
        self.name = name # Сохраняем имя клиента
        self.cargo_weight = cargo_weight # Сохраняем вес груза клиента
        self.is_vip = is_vip # Сохраняем статус VIP
