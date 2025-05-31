class Shape:
    def area(self):
       #Вычисление площади фигуры
        raise NotImplementedError("Метод area() должен быть реализован в подклассе.")

    def perimeter(self):
       #Вычисление периметра фигуры
        raise NotImplementedError("Метод perimeter() должен быть реализован в подклассе.")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * (self.radius ** 2)  # Используем приближенное значение π

    def perimeter(self):
        return 2 * 3.14159 * self.radius  # Используем приближенное значение π


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def area(self):
        # Формула Герона
        s = self.perimeter() / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5


def print_shape_info(shape):
    print(f"Фигура: {type(shape).__name__}")
    print(f"Площадь: {shape.area():.2f}")
    print(f"Периметр: {shape.perimeter():.2f}")
    print('-' * 30)



if __name__ == "__main__":
    shapes = [
        Rectangle(10, 5),
        Circle(7),
        Triangle(3, 4, 5)
    ]

    for shape in shapes:
        print_shape_info(shape)
