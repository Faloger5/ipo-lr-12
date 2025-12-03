class Vehicle:
    # Базовый класс транспортного средства
    def __init__(self, capacity):
        self.vehicle_id = str(uuid.uuid4()) # Генерируем уникальный ID транспорта
        self.capacity = capacity # Сохраняем грузоподъемность
        self.current_load = 0 # Текущая загрузка (изначально 0)
        self.clients_list = [] # Список клиентов, чьи грузы загружены
