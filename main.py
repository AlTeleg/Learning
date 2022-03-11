def count_mid_grade(self):
    try:
        self.mid_grade = (sum(sum(list(self.grades.values()), start=[])))/\
                         (len(sum(list(self.grades.values()), start=[])))
    except ZeroDivisionError:
        self.mid_grade = float(0)
    return self.mid_grade

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.mid_grade = 0
    def __str__(self):
        text = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания:' \
               f' {("{:.1f}".format(count_mid_grade(self)))}\nКурсы в процессе изучения: ' \
               f'{", ".join(map(str,self.courses_in_progress))}\n'\
               f'Завершенные курсы: {", ".join(map(str,self.finished_courses))}'
        return text
    def rate_lect(self,lecturer,course):
        if isinstance(lecturer,Lecturer) and course in lecturer.courses_attached \
                and (course in self.courses_in_progress or course in self.finished_courses):
            grade = 0
            while not 1 <= grade <= 10:
                try:
                    grade = int(input(f'Введите оценку от 1 до 10 для курса <{course}> для лектора '
                                      f'"{lecturer.surname} {lecturer.name}":\n'))
                except ValueError as ve:
                    print("Введено некорректное значение оценки!")
                    continue
            if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
            else:
                    lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __lt__(self, other):
        if not isinstance(other, Student):
            return
        return count_mid_grade(self) < count_mid_grade(other)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    def __str__(self):
        text = f'Имя: {self.name}\nФамилия: {self.surname}'
        return text

class Lecturer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self,name,surname)
        self.grades = {}
        self.mid_grade = 0
    def __str__(self):
        text = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {("{:.1f}".format(count_mid_grade(self)))}'
        return text
    def __lt__(self,other):
        if not isinstance(other,Lecturer):
            return
        return count_mid_grade(self)<count_mid_grade(other)

class Reviewer(Mentor):
    def rate_stud(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached\
                and (course in student.courses_in_progress or course in student.finished_courses):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

def mid_grade_st(student_list,course):
    all_mid_grade = []
    i = 0
    for stud in student_list:
        if course in stud.grades:
            all_mid_grade += stud.grades[course]
            i += len(stud.grades[course])
    try:
        return sum(all_mid_grade)/i
    except ZeroDivisionError:
        return float(0)

def mid_grade_lc(lecturer_list,course):
    all_mid_grade = []
    i = 0
    for lect in lecturer_list:
        if course in lect.grades:
            all_mid_grade += lect.grades[course]
            i += len(lect.grades[course])
    try:
        return sum(all_mid_grade)/i
    except ZeroDivisionError:
        return float(0)


new_student1 = Student('Ruoy', 'Eman', 'male')
new_student1.courses_in_progress += ['Python']
new_student1.courses_in_progress += ['Git']
new_student1.finished_courses += ['Введение в программирование']

new_student2 = Student('Diana', 'Sky', 'female')
new_student2.courses_in_progress += ['SQL']
new_student2.finished_courses += ['Python']
new_student2.finished_courses += ['Git']
new_student2.finished_courses += ['Введение в программирование']

new_lector1 = Lecturer('Some', 'Buddy')
new_lector1.courses_attached += ['Python']
new_lector1.courses_attached += ['Git']

new_lector2 = Lecturer('Any', 'Buddy')
new_lector2.courses_attached += ['SQL']
new_lector2.courses_attached += ['Введение в программирование']


new_reviewer1 = Reviewer("Bob", "Bro")
new_reviewer1.courses_attached += ['Python']
new_reviewer1.courses_attached += ['Git']

new_reviewer2 = Reviewer("Jane", "Sister")
new_reviewer2.courses_attached += ['SQL']
new_reviewer2.courses_attached += ['Введение в программирование']


new_reviewer1.rate_stud(new_student1, "Python", 8)
new_reviewer1.rate_stud(new_student1, "Git", 7)
new_reviewer2.rate_stud(new_student1, "Введение в программирование", 9)
new_reviewer2.rate_stud(new_student2, "SQL", 6)
new_reviewer2.rate_stud(new_student2, "Введение в программирование", 3)
new_reviewer1.rate_stud(new_student2, "Git", 5)

new_student1.rate_lect(new_lector1, "Python")
new_student1.rate_lect(new_lector1, "Git")
new_student2.rate_lect(new_lector1, "Python")
new_student2.rate_lect(new_lector1, "Git")
new_student1.rate_lect(new_lector2, "Введение в программирование")
new_student2.rate_lect(new_lector2, "SQL")
new_student2.rate_lect(new_lector2, "Введение в программирование")

students = [new_student1, new_student2]
lectors = [new_lector1, new_lector2]
reviewers = [new_reviewer1, new_reviewer2]


print(f'{new_reviewer1}\n')
print(f'{new_reviewer2}\n')
print(f'{new_lector1}\n')
print(f'{new_lector2}\n')
print(f'{new_student1}\n')
print(f'{new_student2}\n')

print(f'У {new_lector1.name} {new_lector1.surname} меньше ли средний балл чем у '
      f'{new_lector2.name} {new_lector2.surname} - {new_lector1<new_lector2}')
print(f'У {new_student1.name} {new_student1.surname} меньше ли средний балл чем у '
      f'{new_student2.name} {new_student2.surname} - {new_student1<new_student2}')

print(f'\nСредниий балл у лекторов  по курсу "Python": {"{:.1f}".format(mid_grade_lc(lectors, "Python"))}')
print(f'Средниий балл у студентов  по курсу "Python": {"{:.1f}".format(mid_grade_st(students, "Python"))}')
print(f'\nСредниий балл у лекторов  по курсу "Git": {"{:.1f}".format(mid_grade_lc(lectors, "Git"))}')
print(f'Средниий балл у студентов  по курсу "Git": {"{:.1f}".format(mid_grade_st(students, "Git"))}')
print(f'\nСредниий балл у лекторов  по курсу "SQL": {"{:.1f}".format(mid_grade_lc(lectors, "SQL"))}')
print(f'Средниий балл у студентов  по курсу "SQL": {"{:.1f}".format(mid_grade_st(students, "SQL"))}')
print(f'\nСредниий балл у лекторов  по курсу "Введение в программирование": '
      f'{"{:.1f}".format(mid_grade_lc(lectors, "Введение в программирование"))}')
print(f'Средниий балл у студентов  по курсу "Введение в программирование": '
      f'{"{:.1f}".format(mid_grade_st(students, "Введение в программирование"))}')

