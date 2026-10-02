from SY.symarks import SYMarks
from TY.tymarks import TYMarks


class Student:

    def __init__(self, roll_no, name, sy_marks, ty_marks):
        self.roll_no = roll_no
        self.name = name
        self.sy_marks = sy_marks
        self.ty_marks = ty_marks

    def calculate_grade(self):

        total = self.sy_marks.computer + self.ty_marks.theory

        average = total / 2

        if average >= 70:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 50:
            grade = "C"
        elif average >= 40:
            grade = "Pass Class"
        else:
            grade = "Fail"

        return total, average, grade

    def display(self):

        total, average, grade = self.calculate_grade()

        print("\n----- Student Result -----")
        print("Roll Number :", self.roll_no)
        print("Name        :", self.name)
        print("SY Computer :", self.sy_marks.computer)
        print("TY Theory   :", self.ty_marks.theory)
        print("Total       :", total)
        print("Average     :", average)
        print("Grade       :", grade)


# Creating SYMarks object
sy = SYMarks(75, 80, 70)

# Creating TYMarks object
ty = TYMarks(80, 85)

# Creating Student object
student = Student(101, "Rahul", sy, ty)

# Display result
student.display()