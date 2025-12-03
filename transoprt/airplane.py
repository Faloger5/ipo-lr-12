class Airplane(Vehicle):
    # Класс самолета, наследует Vehicle
    def __init__(self, capacity, max_altitude):
        super().__init__(capacity) # Вызываем конструктор родителя Vehicle
        self.max_altitude = max_altitude # Сохраняем максимальную высоту полета
