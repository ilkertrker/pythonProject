#### Interview Question
#######################
# create a function as a divide_students
# If the index is even , add the student to list
# If the index number is odd, add it to the other list.
# But make these two list as a one list at the return section.

students = ["John", "Mark", "Vanessa", "Marian"]


def divide_students(students):
    groups = [[], []]
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    print(groups)
    return groups


st = divide_students()
st[0]




