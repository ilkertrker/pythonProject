###############
#lambda, map, filter, reduce


def summer (a, b):
    return a + b

summer(12, 3) * 9

new_sum = lambda a, b: a + b

new_sum(4, 5)

#map

salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(x):
    return x * 20 / 100 + x

new_salary(5000)

for salary in salaries:
    print(new_salary(salary))

list(map(new_salary, salaries))
#alternetive
list(map(lambda x: x * 20 / 100 + x, salaries))
list(map(lambda x: x ** 2, salaries))

##Filter


list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(filter(lambda x: x % 2 == 0, list_store))

#reduce

from functools import reduce
list_store = [1, 2, 3, 4]
reduce(lambda a, b: a + b, list_store)


string = "abracadabra"
group = []

for index, letter in enumerate(string,1):
    if index * 2 % 2 == 0:
        group.append(letter)

print(group)

students = ["Denise", "Arsen", "Tony", "Audrey"]

[student[0].upper() if len(student) % 2 != 0 else
 student[0].lower() for student in students]