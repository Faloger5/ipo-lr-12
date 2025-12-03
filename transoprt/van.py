class Van(Vehicle):
    # Класс фургона, наследует Vehicle
    def __init__(self, capacity, is_refrigerated):
        super().__init__(capacity) # Вызываем конструктор родителя Vehicle
        self.is_refrigerated = is_refrigerated # Сохраняем признак наличия холодильника
