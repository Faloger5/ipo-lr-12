class TransportCompany:
    # Класс транспортной компании
    def __init__(self, name):
        self.name = name # Сохраняем название компании
        self.vehicles = [] # Список транспортных средств
        self.clients = [] # Список клиентов
     def __str__(self):
        # Магический метод для строкового представления компании
        return (f"Транспортная компания: {self.name}\n"
                f"Количество транспортных средств: {len(self.vehicles)}\n"
                f"Количество клиентов: {len(self.clients)}")

