class Person:
    def display_person(self):
        print("I am a Person")


class Student(Person):
    def display_student(self):
        print("I am a Student")


s = Student()
s.display_person()
s.display_student()