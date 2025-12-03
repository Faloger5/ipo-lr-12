class Client:
    # Класс клиента, у которого есть имя, вес груза и статус VIP
    def __init__(self, name, cargo_weight, is_vip=False):
        if not isinstance(name, str):  # добавлена проверка типа имени
            raise TypeError("Имя клиента должно быть строкой")
        if not isinstance(cargo_weight, (int, float)):  # добавлена проверка типа веса
            raise TypeError("Вес груза должен быть числом")
        if cargo_weight <= 0:  # добавлена проверка на положительный вес
            raise ValueError("Вес груза должен быть положительным")

        self.name = name  # Сохраняем имя клиента
        self.cargo_weight = cargo_weight  # Сохраняем вес груза клиента
        self.is_vip = is_vip  # Сохраняем статус VIP

    def __str__(self):
        # Магический метод для строкового представления объекта
        return f"Клиент {self.name}, груз: {self.cargo_weight} тонн, VIP: {self.is_vip}"
