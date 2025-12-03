import uuid  # Импортируем модуль для генерации уникальных идентификаторов

class Vehicle:
    # Базовый класс транспортного средства
    def __init__(self, capacity):
        if not isinstance(capacity, (int, float)):  # добавлена проверка типа грузоподъёмности
            raise TypeError("Грузоподъёмность должна быть числом")
        if capacity <= 0:  # добавлена проверка на положительное значение
            raise ValueError("Грузоподъёмность должна быть положительной")

        self.vehicle_id = str(uuid.uuid4())  # Генерируем уникальный ID транспорта
        self.capacity = capacity  # Сохраняем грузоподъемность
        self.current_load = 0  # Текущая загрузка (изначально 0)
        self.clients_list = []  # Список клиентов, чьи грузы загружены

    def load_cargo(self, client):
        # Метод загрузки груза клиента
        if not hasattr(client, "cargo_weight"):
            raise TypeError("У клиента отсутствует атрибут cargo_weight")
        if not isinstance(client.cargo_weight, (int, float)):
            raise TypeError("Вес груза должен быть числом")
        if self.current_load + client.cargo_weight > self.capacity:
            raise ValueError("Груз превышает грузоподъемность")

        self.current_load += client.cargo_weight  # Увеличиваем текущую загрузку
        self.clients_list.append(client)  # Добавляем клиента в список

    def __str__(self):
        # Магический метод для строкового представления транспорта
        client_names = [c.name for c in self.clients_list]
        return (f"ID транспорта: {self.vehicle_id}\n"
                f"Грузоподъемность: {self.capacity} тонн\n"
                f"Текущая нагрузка: {self.current_load} тонн\n"
                f"Клиенты: {client_names}")
