import uuid # Импортируем модуль для генерации уникальных идентификаторов

class Client:
    # Класс клиента, у которого есть имя, вес груза и статус VIP
    def __init__(self, name, cargo_weight, is_vip=False):
        self.name = name # Сохраняем имя клиента
        self.cargo_weight = cargo_weight # Сохраняем вес груза клиента
        self.is_vip = is_vip # Сохраняем статус VIP

    def __str__(self):
        # Магический метод для строкового представления объекта
        return f"Клиент {self.name}, груз: {self.cargo_weight} тонн, VIP: {self.is_vip}"


class Vehicle:
    # Базовый класс транспортного средства
    def __init__(self, capacity):
        self.vehicle_id = str(uuid.uuid4()) # Генерируем уникальный ID транспорта
        self.capacity = capacity # Сохраняем грузоподъемность
        self.current_load = 0 # Текущая загрузка (изначально 0)
        self.clients_list = [] # Список клиентов, чьи грузы загружены

    def load_cargo(self, client):
        # Метод загрузки груза клиента
        if not hasattr(client, "cargo_weight"):
            raise TypeError("У клиента отсутствует атрибут cargo_weight")
        if not isinstance(client.cargo_weight, (int, float)):
            raise TypeError("Вес груза должен быть числом")
        if self.current_load + client.cargo_weight > self.capacity:
            raise ValueError("Груз превышает грузоподъемность")
        self.current_load += client.cargo_weight # Увеличиваем текущую загрузку
        self.clients_list.append(client) # Добавляем клиента в список

    def __str__(self):
        # Магический метод для строкового представления транспорта
        client_names = [c.name for c in self.clients_list]
        return (f"ID транспорта: {self.vehicle_id}\n"
                f"Грузоподъемность: {self.capacity} тонн\n"
                f"Текущая нагрузка: {self.current_load} тонн\n"
                f"Клиенты: {client_names}")
