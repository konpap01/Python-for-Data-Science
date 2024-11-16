
''' Let's design a course registration system, where the requirements will be: ''' 

''' 1. Create a Course class, where each course has a name, a description and a list of enrolled students. You'll need to implement the next methods:
    - Add a student to the course.
    - Remove a student from the course.
    - Show all students in the course. ''' 

class course:
   
    def __init__(self, name, desc, enr):
        self.name = name
        self.description = desc
        self.students = enr

    def add_student(self, stud):
        self.students.append(stud)

    def remove_student(self, stud):
        self.students.remove(stud)
    
    def show_all(self):
        print(self.students)

# Testing: 
course1 = course("Math", "Algebra", ["John", "Konstantinos"])
course1.add_student("George")
course1.add_student("Nick")
course1.remove_student("John")
course1.show_all()


''' 2. Create a Student class, where each student has a name, ID number, address and a list of enrolled courses with the following methods:
    - Enroll in a course.
    - Drop a course.
    - Show all registered student courses. ''' 

class student: 
    def __init__(self, name, ID, address, courses):
        self.name = name
        self.ID = ID
        self.address = address
        self.courses = courses
    
    def enroll(self, course):
        self.courses.append(course)

    def drop(self, course):
        self.courses.remove(course)

    def show_all(self):
        print(self.courses)


#Testing:
stud1 = student("Konstantinos", 12345, "Carrer Roma", ["Math", "CompSci"])
stud1.enroll("AI")
stud1.drop("Math")
stud1.show_all()


''' 3. Create a central class that manages courses and students, Registration class, where you have a list of students and a list of courses, and methods:
    - Enroll in a course.
    - Drop a course.
    - Show all the enrolled courses.
    - Show all the students.

    4. Let's add grades to each student's course and create method that yields the GPA given a student name or ID. '''

class registration:
    def __init__(self, students, courses):
        self.students = students
        self.courses = courses
        self.grades = {}

    def enroll(self, student, course):
        student.enroll(course.name)
        course.add_student(student.name)
        if student.name not in self.grades:
            self.grades[student.name] = {}
        print(f"{student.name} has been enrolled in {course.name}.")

    def drop(self, student, course):
        student.drop(course.name)
        course.remove_student(student.name)
        if student.name in self.grades and course.name in self.grades[student.name]:
            del self.grades[student.name][course.name]
        print(f"{student.name} has been dropped from {course.name}.")

    def show_courses(self):
        for course in self.courses:
            course.show_all()

    def show_students(self):
        for student in self.students:
            student.show_all()

    def add_grade(self, student, course, grade):
        if student.name in self.grades and course.name in student.courses:
            self.grades[student.name][course.name] = grade
            print(f"Grade {grade} added for {student.name} in {course.name}.")
        else:
            print(f"{student.name} is not enrolled in {course.name}.")

    def calculate_gpa(self, student_name):
        if student_name in self.grades:
            student_grades = self.grades[student_name]
            if student_grades:
                total = sum(student_grades.values())
                gpa = total / len(student_grades)
                return round(gpa, 2)
        return 0.0

#Testing:

course1 = course("Math", "Algebra", ["John", "Konstantinos"])
course2 = course("CompSci", "Programming", [])

stud1 = student("Konstantinos", 12345, "Carrer Roma", ["Math", "CompSci"])
stud2 = student("Alice", 67890, "Carrer Paris", [])

reg = registration([stud1, stud2], [course1, course2])

reg.enroll(stud1, course2)
reg.enroll(stud2, course1)

reg.add_grade(stud1, course2, 85)
reg.add_grade(stud2, course1, 90)

print(f"GPA for Konstantinos: {reg.calculate_gpa('Konstantinos')}")
print(f"GPA for Alice: {reg.calculate_gpa('Alice')}")

print("\nCourses:")
reg.show_courses()

print("\nStudents:")
reg.show_students()




        



