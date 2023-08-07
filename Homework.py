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

    def _average_value_of_grades(self):
        x = []
        for grades in self.grades.values():
            x += grades
        if len(x) > 0:
            x = sum(x) / len(x)
            return x
        else:
            return 'Оценки для вычисления среднего показателя отсутствуют'

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

    def __str__(self):
        res = (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания:{self._average_value_of_grades()}\n'
        f'Курсы в процессе изучения {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}')
        return res

    def __lt__(self, other):
        return self._average_value_of_grades() < other._average_value_of_grades()


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
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{self._average_value_of_lectionsgrades()}'
        return res

    def _average_value_of_lectionsgrades(self):
        x = []
        for grades in self.lectionsgrades.values():
            x += grades
        if len(x) > 0:
            return sum(x) / len(x)
        else:
            return 'Отсутствуют оценки за лекции для подсчета среднего показателя'

    def __lt__(self, other):
       return self._average_value_of_lectionsgrades() < other._average_value_of_lectionsgrades()


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

def average_value_of_students_grades(students, course):
    x = []
    y = 0
    for student in students:
        if course in student.grades.keys():
            x.append(sum(student.grades[course]) / len(student.grades[course]))
            y += 1
    return sum(x)/y

def average_value_of_lections_grades(lecturers, course):
    x = []
    y = 0
    for lecturer in lecturers:
        if course in lecturer.lectionsgrades.keys():
            x.append(sum(lecturer.lectionsgrades[course]) / len(lecturer.lectionsgrades[course]))
            y += 1
    if y > 0:
        return sum(x) / y
    else:
        return 'Оценки по выбранному предмету у лекторов отсутствуют'


worst_student = Student('Bill', 'Klinton', 'Male')
best_student = Student('Kalem', 'Drake', 'Female')
best_lecturer = Lecturer('Chaos', 'Knight')
worst_lecturer = Lecturer('Bred', 'Pitt')
best_reviewer = Reviewer('Amanda', 'Banx')
worst_reviewer = Reviewer('Nick', 'Cage')
best_lecturer.courses_attached += ['Git', 'OOP']
worst_student.courses_in_progress += ['Git', 'OOP']
worst_student.rate_lection(best_lecturer, 'Git', 9)
worst_student.rate_lection(best_lecturer, 'Git', 3)
worst_student.rate_lection(best_lecturer, 'Git', 4)
worst_student.rate_lection(best_lecturer, 'OOP', 9)
worst_student.rate_lection(worst_lecturer, 'Git', 1)
best_student.rate_lection(worst_lecturer, 'Git', 3)
worst_student.rate_lection(best_lecturer, 'OOP', 4)
best_lecturer.courses_attached += ['Programming']
worst_student.courses_in_progress += ['Programming']
worst_student.rate_lection(best_lecturer, 'Programming', 9)
print(worst_lecturer)
print(best_lecturer)
print(worst_student)
best_student.courses_in_progress += ['OOP', 'Git']
best_reviewer.rate_hw(best_student, 'Git', 6)
print(best_student)
print(best_student > worst_student)
worst_lecturer.courses_attached += ['Programming']
worst_student.rate_lection(worst_lecturer, 'Programming', 10)
print(best_lecturer)
print(worst_lecturer)
print(best_lecturer < worst_lecturer)
print(average_value_of_students_grades([worst_student, best_student], 'Git'))
print(average_value_of_lections_grades([worst_lecturer], 'Git'))
