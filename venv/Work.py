class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = []

    def rate_lec(self, lecturer, course, appraisal):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.appraisals:
                lecturer.appraisals[course] += [appraisal]
            else:
                lecturer.appraisals[course] = [appraisal]
        else:
            return 'Ошибка'

    def avg(self, student, grade):
        for student, grade in self.grades[grade].values():
            self.average_grade = float(sum(grade) / len(grade))

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade}\nКурсы в процессе изучения: {" ".join(self.courses_in_progress)}\nЗавершенные курсы: {" ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if isinstance(other, Student):
            print('Not a Student')
            return
        return self.average_grade < other.average_grade


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


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


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.appraisals = {}
        self.average_appraisal = []

    def avg(self, lecturer, appraisal):
        for lecturer,  appraisal in self.appraisals[appraisal].values():
            self.average_appraisal = float(sum(appraisal) / len(appraisal))

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_appraisal}'
        return res

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            print('Not a Lecturer')
            return
        return self.average_appraisal < other.average_appraisal


some_lecturer_1 = Lecturer('Ivan', 'Moody')
some_lecturer_1.courses_attached = ['Python', 'Javascript']

some_lecturer_2 = Lecturer('Lizzy', 'Hale')
some_lecturer_2.courses_attached = ['Java', 'C++']

some_student_1 = Student('Matt', 'Heafy', 'Male')
some_student_1.finished_courses += ['Javascript']
some_student_1.courses_in_progress += ['Python']
some_student_1.rate_lec(some_lecturer_1, 'Python', 9)

some_student_2 = Student('Taylor', 'Momsen', 'Female')
some_student_2.finished_courses += ['Python']
some_student_2.courses_in_progress += ['Java']
some_student_2.rate_lec(some_lecturer_2, 'Java', 10)

some_student_3 = Student('Bruce', 'Dickinson', 'Male')
some_student_3.finished_courses += ['Python']
some_student_3.courses_in_progress += ['Java']
some_student_3.rate_lec(some_lecturer_2, 'Java', 8)

some_reviewer_1 = Reviewer('Maria', 'Brink')
some_reviewer_1.rate_hw(some_student_1, 'Python', 10)
some_reviewer_2 = Reviewer('Zoltan', 'Bathory')
some_reviewer_2.rate_hw(some_student_2, 'Java', 7)
some_reviewer_2.rate_hw(some_student_3, 'Java', 6)

print(some_student_1)
print(some_student_2)
print(some_student_3)
print(some_reviewer_1)
print(some_reviewer_2)
print(some_lecturer_1)
print(some_lecturer_2)

print(some_student_1.grades)
print(some_student_2.grades)
print(some_student_3.grades)

print(some_lecturer_1.appraisals)
print(some_lecturer_2.appraisals)

studentlist = []
studentlist.append(some_student_1)
studentlist.append(some_student_2)
studentlist.append(some_student_3)

lecturerlist = []
lecturerlist.append(some_lecturer_1)
lecturerlist.append(some_lecturer_2)

def studentgrade(studentlist, course):
    for student in studentlist:
        if course in student.grades[courses] == [Java]:
            average_grade = float(sum(grade) / len(grade))
        else:
            return 'Error'
    return average_grade

def lecturergrade(lecturerlist, course):
    for lecturer in lecturerlist:
        if course in self.appraisals[courses] == [Python]:
            average_appraisal = float(sum(grade) / len(grade))
        else:
            return 'Error'
    return average_appraisal

print(studentgrade)
print(lecturergrade)