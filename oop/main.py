class Student:
    def __init__(self, name, regNumber, grade):
        self.name = name
        self.regNumber = regNumber
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, course_name, max_Students):
        self.course_name = course_name
        self.maxStudents = max_Students
        self.passGrade = 50
        self.acceptedStudents = []

    def add_Students(self, student):
        if self.maxStudents > len(self.acceptedStudents):
            if self.passGrade <= student.get_grade():
                self.acceptedStudents.append(student)
                return self.acceptedStudents

            else:
                return "your grade is too low"
        else:
            return 'the ' + self.course_name + " is full please apply next year"


s1 = Student('charles Madhuku', 'R219736J', 97)
s2 = Student('Stiles', 'R2378Jk', 44)
s3 = Student('darkWarker', 'R23743Jk', 74)
s4 = Student('Stilinsiki', 'R2378io', 91)

course = Course('Data Science', 2,)

print(course.add_Students(s1))
print(course.add_Students(s2))
print(course.add_Students(s3))
print(course.add_Students(s4))
