"""ITF 08 Final Project Attendance System
# TODO 1 Enter your name and submission date
Name : Ola Mohammed Abo Kwaik
Delivery Date :31/8/2023
"""

# TODO 2 Define Course Class and define constructor with
# course_id (generated using uuid4) ,
# course name (user_input) and
# course mark (user_input)
import uuid


class Course:
    def __init__(self, course_name, course_mark):
        self.course_id = str(uuid.uuid4())
        self.course_name = course_name
        self.course_mark = course_mark


class Student:
    # TODO 3 define static variable indicates total student count
    total_students = 0

    # TODO 4 define a constructor which includes
    # student_id (unique using uuid module)
    # student_name (user input)
    # student_age (user input)
    # student_number (user_input)
    # courses_list (List of Course Objects)
    def __init__(self, student_name, student_age, student_number):
        self.student_id = str(uuid.uuid4())
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = str(student_number)  # Convert to string
        self.courses_list = []
        students.append(self)

        pass

    # TODO 5 define a method to enroll new course to student courses list
    def enroll_course(self, course_name, course_mark):
        course = Course(course_name, course_mark)
        self.courses_list.append(course)

    # method to get_student_details as dict
    def get_student_details(self):
        return {
            "Student ID": self.student_id,
            "Student Name": self.student_name,
            "Student Age": self.student_age,
            "Student Number": self.student_number,

        }

    # method to get_student_courses
    def get_student_courses(self):
        # TODO 6 print student courses with their marks
        for course in self.courses_list:
            print(f"Course: {course.course_name}, Mark: {course.course_mark}")
        pass

    # method to get student_average as a value
    def get_student_average(self):
        # TODO 7 return the student average
        if not self.courses_list:
            return 0
        total_mark = sum(course.course_mark for course in self.courses_list)
        return total_mark / len(self.courses_list)
        pass


def show_student_courses():
    student_number = input("Enter Student Number to show courses: ")
    for student in students:
        if student.student_number == student_number:
            student.get_student_courses()
            break
    else:
        print("Student Not Found.")


# in Global Scope
# TODO 8 declare empty students list
students = []
student1 = Student('Ahmad', "10", '25')
student2 = Student('waseem', "15", '12')
student3 = Student('hala', "20", '9')

while True:
    try:

        # TODO 9 handle Exception for selection input
        selection = int(input("\n \n1. Add New Student\n"
                              "2. Delete Student\n"
                              "3. Display Student\n"
                              "4. Get Student Average\n"
                              "5. Add Course to Student with Mark\n"
                              "6. show student courses \n"
                              "7.Exit\n"
                              '\n\n input number please : '))

        if selection == 1:

            # TODO 10 make sure that Student number is not exists before
            student_number = input("Enter Student Number")
            student_exists = any(student.student_number == student_number for student in students)
            if not student_exists:

                student_name = input("Enter Student Name")
                while True:
                    try:
                        student_age = int(input("Enter Student Age"))
                        break
                    except ValueError:
                        print("Invalid Value")

                # TODO 11 create student object and append it to students list
                student = Student(student_name, student_age, student_number)
                students.append(student)
                print("Student Added Successfully")
            else:
                print("Student Number already exists.")

        elif selection == 2:
            student_number = input("Enter Student Number")
            # TODO 12 find the target student using loops and delete it if exist , if not print ("Student Not Exist")
            for student in students:
                if student.student_number == student_number:
                    students.remove(student)
                    print(f"Student {student.student_name} with number {student.student_number} deleted.")
                    break
            else:
                print("Student Not Found.")
        elif selection == 3:
            student_number = input("Enter Student Number")
            # TODO 13 find the target student using loops and print student detials  if exist , if not print ("Student Not Exist")
            for student in students:
                if student.student_number == student_number:
                    details = student.get_student_details()
                    print("Student Details:")
                    for key, value in details.items():
                        print(f"{key}: {value}")

                    for student in students:
                        if student.student_number == student_number:
                            student.get_student_courses()
                            break
                    break

            else:
                print("Student Not Found.")
        elif selection == 4:
            student_number = input("Enter Student Number")
            # TODO 14 find the target student using loops and get student average  if exist , if not print ("Student Not Exist")
            for student in students:
                if student.student_number == student_number:
                    average = student.get_student_average()
                    print(f"Student Average: {average}")
                    break
            else:
                print("Student Not Found.")
        elif selection == 5:
            student_number = input("Enter Student Number")
            # TODO 15 ask user to enter course name and course mark then create coures object then append it to target student courses
            for student in students:
                if student.student_number == student_number:
                    course_name = input("Enter Course Name: ")
                    while True:
                        try:
                            course_mark = float(input("Enter Course Mark: "))
                            break
                        except ValueError:
                            print("Invalid Value")
                    student.enroll_course(course_name, course_mark)
                    print(f"Course {course_name} with mark {course_mark} added to {student.student_name}'s courses.")
                    break
            else:
                print("Student Not Found.")
        elif selection == 6:
            show_student_courses()
        elif selection == 7:
            # Exit the program
            break
        else:
            print("Invalid selection. Please choose a valid option.")


    except ValueError:
        print("Invalid input. Please enter a number.")
        # TODO 16 call a function to exit the program
