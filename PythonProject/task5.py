class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        if isinstance(grade, (int, float)) and 0 <= grade <= 10:
            self.grades.append(grade)
        else:
            raise ValueError("Допустимое значение от 0 до 10")

    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        average_grade = self.get_average()
        print(f"Имя студента: {self.name}")
        print(f"ID студента: {self.student_id}")
        print(f"Оценки: {self.grades}")
        print(f"Средний балл: {average_grade:.2f}")

    def __str__(self):
        return f"Студент: {self.name}, ID: {self.student_id}, Средний балл: {self.get_average():.2f}"

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.student_id == other.student_id
        return False

    def __len__(self):
        return len(self.grades)


# Пример использования класса Student
if __name__ == "__main__":
    student1 = Student("Иван Иванов", "12345")
    student1.add_grade(8)
    student1.add_grade(9)
    student1.add_grade(7)

    student2 = Student("Петр Петров", "12346")
    student2.add_grade(6)
    student2.add_grade(5)

    # Вывод информации о студентах
    student1.display_info()
    print(student1)  # Использование __str__

    student2.display_info()
    print(student2)  # Использование __str__

    # Сравнение студентов
    print(student1 == student2)  # False
    print(student1 == Student("Иван Иванов", "12345"))  # True

    # Количество оценок
    print(f"Количество оценок у {student1.name}: {len(student1)}")  # Использование __len__
