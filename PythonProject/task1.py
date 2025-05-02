class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        if isinstance(grade, (int, float)) and 0 <= grade <= 10:
            self.grades.append(grade)
        else:
            raise ValueError("Допустимое значчение от 1 до 10")

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


student = Student("Иван Иванов", "12345")
student.add_grade(8)
student.add_grade(9)
student.add_grade(7)
student.display_info()