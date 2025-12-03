from .vehicle import Vehicle  # добавлен импорт родительского класса

class Airplane(Vehicle):
    # Класс самолета, наследует Vehicle
    def __init__(self, capacity, max_altitude):
        super().__init__(capacity)  # Вызываем конструктор родителя Vehicle
        if not isinstance(max_altitude, int):  # добавлена проверка типа высоты
            raise TypeError("Максимальная высота должна быть целым числом")
        self.max_altitude = max_altitude  # Сохраняем максимальную высоту полета
        
     def __str__(self):
        return super().__str__() + f"\nМаксимальная высота: {self.max_altitude} м" # Выводим максимальную высоту
