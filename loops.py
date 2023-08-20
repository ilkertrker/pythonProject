##################
####loops#########
##################

###for  loop

students = ["John", "Mark", "Vanessa", "Mariam"]

students[0]
students[3]
students[2]

for student in students:
    print(student)

####### level2

students = ["John", "Mark", "Vanessa", "Mariam"]

students[0]
students[3]
students[2]


for student in students:
    print(student.upper())

#lvl3

salaries = [1000, 2000, 3000, 4000]

for salary in salaries:
    print(int(salary*20/100 + salary))


for salary in salaries:
    print(int(salary*50/100 + salary))

def new_salary(salary, rate):
    return int(salary*rate/100 + salary)

new_salary(1000,20)
new_salary(2000, 20)

for salary in salaries:
    print(new_salary(salary,10))

salaries2 = [100020, 2000, 15550, 25556]


for salary in salaries2:
    print(new_salary(salary,10))


for salary in salaries:
    if salary >= 3000:
        print(new_salary(salary,15))
    else:
        print(new_salary(salary,20

        ########################
        # break & continue & while
        #########################

salaries = [1000, 2000, 2020, 6000]

for salary in salaries:
    if salary == 2020:
        break
    print(salary)


for salary in salaries:
    if salary == 2000:
        continue
    print(salary)


number = 1
while number < 5:
    print(number)
    number += 1