import json

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        a = ''
        for i in self.marks:
            a += str(i) + ", "
        return f"Студент: {self.name} {a[:-2]}"

    def add_mark(self, mark):
        self.marks.append(mark)

    def delete_mark(self, index):
        self.marks.pop(index)

    def edit_mark(self, index, new_mark):
        self.marks[index] = new_mark

    def average_mark(self):
        return round(sum(self.marks) / len(self.marks), 2)

    @classmethod
    def dump_to_json(cls, stud, filename):
        try:
            data = json.load(open(filename))
        except FileNotFoundError:
            data = []

        data = {'name': stud.name, 'marks': stud.marks}
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)


class Group:
    def __init__(self, students, group):
        self.students = students
        self.group = group

    def __str__(self):
        a = ''
        for i in self.students:
            a += str(i) + "\n"
        return f"Группа: {self.group}\n{a}"

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, index):
        return self.students.pop(index)

    @classmethod
    def change_group(cls, group1, group2, index):
        return group2.add_student(group1.remove_student(index))


st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
st2 = Student('Nikolaenko', [2, 3, 5, 4, 2])
st3 = Student('Birukov', [3, 5, 3, 2, 5, 4])
sts = [st1, st2]

Student.dump_to_json(st1, 'student.json')
Student.dump_to_json(st2, 'student.json')
# my_group = Group(sts, "ГК Python")
# print(my_group)
# my_group.add_student(st3)
# print(my_group)
# my_group.remove_student(1)
# print(my_group)
#
# group22 = [st2]
# my_group2 = Group(group22, "ГК Web")
# print(my_group2)
#
# Group.change_group(my_group, my_group2, 0)
# print(my_group)
# print(my_group2)