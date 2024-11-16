
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
    - Show all the students. '''

class registration:
    def __init__(self, students, courses):
        self.students = students
        self.courses = courses

    def enroll(self, course):
        self.courses.append(course)

    def drop(self, course):
        self.courses.remove(course)

    def show_courses(self):
        print(self.courses)

    def show_students(self):
        print(self.students)

#Testing: 
reg = registration(["kon", "mike"], ["math", "physics", "CompSci"])

reg.enroll("AI")
reg.drop("physics")

reg.show_students()
reg.show_courses()




        



