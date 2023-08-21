###
##basic

1 == 1
1 == 2

#if
if 1 == 1:
    print("something")

if 1 == 2:
    print("something")

number = 10

if number == 10:
    print("number is 10")

number = 20

##Number check function

def num_check(number):
    if number == 10:
        print("number is 10")

num_check(12)

####Else########

def num_check(number):
    if number == 10:
        print("number is 10")
    else:
        print("number is not 10")


num_check(12)


########El_if###


def number_check(number):
    if number > 10:
        print("number is grater than 10")
    elif number < 10:
        print("number is less than 10")
    else:
        print("equal to 10")

number_check(10)



################################################
### lambda, map, filter, reduce
####################################

def summer(a, b):
    return a + b
summer(1, 3) * 9

new_sum = lambda a, b: a + b
new_sum(4, 5)

### map function

salaries = [100, 2000, 3000, 4000, 5000]
