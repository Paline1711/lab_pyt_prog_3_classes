class Temperature:
    def __init__(self, celsius=0):
        self._celsius = None
        self.celsius = celsius  # через сеттер с валидацией

    @property
    def celsius(self):
        """Геттер температуры в градусах Цельсия"""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Сеттер с валидацией для температуры в градусах Цельсия"""
        if not isinstance(value, (int, float)):
            raise TypeError("Температура должна быть числом")
        # Валидацию по диапазону можно добавить, если нужно
        self._celsius = value

    @property
    def fahrenheit(self):
        """Динамическое свойство для температуры в Фаренгейтах"""
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        """Сеттер для температуры в Фаренгейтах"""
        if not isinstance(value, (int, float)):
            raise TypeError("Температура должна быть числом")
        self._celsius = (value - 32) * 5 / 9


# Пример равботы
if __name__ == "__main__":
    temp = Temperature(25)
    print(f"Температура в Цельсиях: {temp.celsius}")
    print(f"Температура в Фаренгейтах: {temp.fahrenheit}")

    temp.fahrenheit = 86
    print(f"Установлено значение 86°F, это {temp.celsius:.2f}°C")

