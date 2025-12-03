from .vehicle import Vehicle  # добавлен импорт родительского класса

class Van(Vehicle):
    # Класс фургона, наследует Vehicle
    def __init__(self, capacity, is_refrigerated):
        super().__init__(capacity)  # Вызываем конструктор родителя Vehicle
        if not isinstance(is_refrigerated, bool):  # добавлена проверка типа
            raise TypeError("is_refrigerated должен быть True или False")
        self.is_refrigerated = is_refrigerated  # Сохраняем признак наличия холодильника
        
    def __str__(self):
        return super().__str__() + f"\nХолодильник: {self.is_refrigerator}" # Выводим параметр холодильника
