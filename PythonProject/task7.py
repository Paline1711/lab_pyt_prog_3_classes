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


class Teacher:
    def __init__(self, name, teacher_id, subject):
        self.name = name
        self.teacher_id = teacher_id
        self.subject = subject

    def display_info(self):
        print(f"Имя преподавателя: {self.name}")
        print(f"ID преподавателя: {self.teacher_id}")
        print(f"Предмет: {self.subject}")


class Assistant(Student, Teacher):
    def __init__(self, name, student_id, teacher_id, subject):
        # Инициализация Student части
        Student.__init__(self, name, student_id)
        # Инициализация Teacher части
        Teacher.__init__(self, name, teacher_id, subject)

    def help_student(self):
        print(f"Ассистент {self.name} помогает студентам по предмету {self.subject}.")


# Пример работы
if __name__ == "__main__":
    assistant = Assistant("Алексей Смирнов", "S123", "T456", "Математика")
    assistant.display_info()  # Это вызовет display_info из Student по MRO
    assistant.help_student()
    assistant.add_grade(9)
    assistant.display_info()