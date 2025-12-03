class TransportCompany:
    # Класс транспортной компании
    def __init__(self, name):
        self.name = name # Сохраняем название компании
        self.vehicles = [] # Список транспортных средств
        self.clients = [] # Список клиентов
