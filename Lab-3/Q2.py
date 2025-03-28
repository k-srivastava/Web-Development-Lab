from typing import Self


class Student:
    def __init__(self, name: str, roll_number: int, department: str, address: str, gender: str, marks: list[int]):
        self.name = name
        self.roll_number = roll_number
        self.department = department
        self.address = address
        self.gender = gender
        self.marks = marks

    def marks_total(self) -> int:
        return sum(self.marks)

    def did_fail(self) -> bool:
        return self.marks_total() < 10

    @classmethod
    def create_student(cls) -> Self:
        name = input('Enter the name: ')
        roll_number = int(input('Enter the roll number: '))
        department = input('Enter the department: ')
        address = input('Enter the address: ')
        gender = input('Enter the gender: ')
        marks = [int(number) for number in input('Enter the marks in three subjects: ').split()]

        return cls(name, roll_number, department, address, gender, marks)


def main():
    students = []

    for i in range(10):
        print(f'Student [{i}]')
        students.append(Student.create_student())

    for student in students:
        print(f'Total Marks: {student.marks_total()}')

    max_marks = max([student.marks_total() for student in students])
    min_marks = min([student.marks_total() for student in students])

    print(f'Max Marks: {max_marks}')
    print(f'Min Marks: {min_marks}')


if __name__ == '__main__':
    main()
