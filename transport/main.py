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


class Airplane(Vehicle):
    # Класс самолета, наследует Vehicle
    def __init__(self, capacity, max_altitude):
        super().__init__(capacity) # Вызываем конструктор родителя Vehicle
        self.max_altitude = max_altitude # Сохраняем максимальную высоту полета


class Van(Vehicle):
    # Класс фургона, наследует Vehicle
    def __init__(self, capacity, is_refrigerated):
        super().__init__(capacity) # Вызываем конструктор родителя Vehicle
        self.is_refrigerated = is_refrigerated # Сохраняем признак наличия холодильника


class TransportCompany:
    # Класс транспортной компании
    def __init__(self, name):
        self.name = name # Сохраняем название компании
        self.vehicles = [] # Список транспортных средств
        self.clients = [] # Список клиентов

    def add_vehicle(self, vehicle):
        # Метод добавления транспорта
        if not hasattr(vehicle, "capacity"):
            raise TypeError("Объект не является транспортным средством")
        self.vehicles.append(vehicle) # Добавляем транспорт в список

    def list_vehicles(self):
        # Метод возвращает список всех транспортных средств
        return self.vehicles

    def add_client(self, client):
        # Метод добавления клиента
        if not hasattr(client, "cargo_weight"):
            raise TypeError("Объект не является клиентом")
        self.clients.append(client) # Добавляем клиента в список

    def optimize_cargo_distribution(self):
        # Метод оптимизации распределения грузов
        sorted_clients = sorted(self.clients, key=lambda c: not c.is_vip) # VIP-клиенты первыми
        sorted_vehicles = sorted(self.vehicles, key=lambda v: v.capacity, reverse=True) # Сортируем транспорт по вместимости

        for client in sorted_clients:
            loaded = False # Флаг загрузки
            for vehicle in sorted_vehicles:
                try:
                    vehicle.load_cargo(client) # Пытаемся загрузить клиента
                    loaded = True
                    break # Выходим из цикла по транспорту
                except ValueError:
                    continue # Пробуем следующий транспорт
            if not loaded:
                print(f"Не удалось загрузить клиента {client.name}: груз превышает вместимость всех транспортов")

    def __str__(self):
        # Магический метод для строкового представления компании
        return (f"Транспортная компания: {self.name}\n"
                f"Количество транспортных средств: {len(self.vehicles)}\n"
                f"Количество клиентов: {len(self.clients)}")
