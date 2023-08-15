# Functions#

# basic function
print("a", "b", sep="__")


# multiply by 2#

def calculate(x):
    print(x * 2)


calculate(5)

# Two parameter function#

def summer(arg1, arg2):
    print(arg1 + arg2)


summer(6, 8)


summer(arg2=6, arg1=8)


#######################
## Function Statement##
#######################

# def function_name(parameters/arguments):
#     statements (funtion body)

def say_hi(string):
    print()
    print("hi")
    print("Supp?")


say_hi("oooi")


def multiplication(a, b):
    c = a * b
    print(c)


multiplication(10, 9)


#Girilen Değerleri Liste içinde sakla

list_store = []

def add_element(a, b):
    c = a * b
    list_store.append(c)
    print(list_store)

print(list_store)
add_element(3, 1)
add_element(100, 12)
add_element(3, 4)
###results
print(list_store)


##########Defult Parameters/Arguments

def divide(a, b):
    print(a / b)

divide(1, 2)

