class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        if isinstance(grade, (int, float)) and 0 <= grade <= 10:
            self.grades.append(grade)
        else:
            raise ValueError("Допустимое значение от 0 до 10.")

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

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        self.students = []

    def add_student(self, student):
        if isinstance(student, Student):
            if student not in self.students:
                self.students.append(student)
                print(f"Студент {student.name} добавлен.")
            else:
                print(f"Студент {student.name} уже в списке.")
        else:
            raise TypeError("Можно добавлять только объекты Student.")

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            print(f"Студент {student.name} удален.")
        else:
            print(f"Студент {student.name} не найден в списке.")

    def list_students(self):
        if not self.students:
            print("Список студентов пуст.")
            return
        print(f"Студенты преподавателя {self.name}:")
        for student in self.students:
            print(f"- {student.name} (ID: {student.student_id})")


if __name__ == "__main__":
    teacher = Teacher("Анна Петровна", 40, "Математика")
    student1 = Student("Иван Иванов", "12345")
    student2 = Student("Мария Сидорова", "67890")

    teacher.add_student(student1)
    teacher.add_student(student2)
    teacher.list_students()

    teacher.remove_student(student1)
    teacher.list_students()