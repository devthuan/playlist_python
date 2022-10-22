
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
    
def get_many_data():
    students = []
    total = int(input("Enter total student: "))
    for i in range(total):
        studs = get_data()
        students.append(studs)

    return students

def print_info(data):
    print("----------------- \n")
    print("Name: ", data.name)
    print("ID student: ", data.id_stud)
    print("major: ", data.major)

def print_infos(stud):    
    for i in range(len(stud)):
        print_info(stud[i])


def main():
    stud = get_many_data()

    print_infos(stud)

main()