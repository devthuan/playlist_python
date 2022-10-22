
from unicodedata import name


class Student():
    def __init__(self, name, id_stud, major):
        self.name = name
        self.id_stud = id_stud
        self.major = major

def get_data():
    name = input("Enter your name: ")
    id_stud = input("Enter your id_stud: ")
    major = input("Enter your major : ")
    student = Student(name, id_stud, major)

    return student
    

def print_info(data):
    print("Name: ", data.name)
    print("ID student: ", data.id_stud)
    print("major: ", data.major)



def main():
    stud = get_data()

    print_info(stud)

main()