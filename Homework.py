class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lection(self, lecturer, course, grade):
        if ((isinstance(lecturer, Lecturer) and
             course in self.courses_in_progress and
             course in lecturer.courses_attached)):
            if course in lecturer.lectionsgrades.keys():
                lecturer.lectionsgrades[course] += [grade]
            else:
                lecturer.lectionsgrades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lectionsgrades = {}

    def __str__(self):
        x = self.lectionsgrades
        print(x)
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{(sum(x))/(len(x))}'
        return res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


worst_student = Student('Bill', 'Klinton', 'Male')
best_lecturer = Lecturer('Chaos', 'Knight')
best_lecturer.courses_attached += ['Git']
worst_student.courses_in_progress += ['Git']
worst_student.rate_lection(best_lecturer, 'Git', 9)
worst_student.rate_lection(best_lecturer, 'Git', 3)
worst_student.rate_lection(best_lecturer, 'Git', 4)
best_lecturer.courses_attached += ['OOP']
worst_student.courses_in_progress += ['OOP']
print(best_lecturer.courses_attached)
print(best_lecturer.lectionsgrades)
worst_student.rate_lection(best_lecturer, 'OOP', 9)
