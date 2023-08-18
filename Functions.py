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

# Girilen Değerleri Liste içinde sakla

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


####Samples

# Information from the street lamps / varms,moisture,charger

# DRY


def calculate(varm, moisture, charge):
    print((varm + moisture) / charge)


calculate(30, 50, 11)


######Return
def calculate(varm, moisture, charge):
    print((varm + moisture) / charge)


calculate(30, 50, 11) * 10  # hatalı kullanım


def calculate(varm, moisture, charge):
    return (varm + moisture) / charge


calculate(98, 12, 77)
calculate(98, 12, 77) * 10


def calculate(varm, moisture, charge):
    varm = varm * 2
    moisture = moisture * 2
    charge = charge * 2
    output = (varm + moisture) / charge

    return varm, moisture, charge, output


type(calculate(98, 12, 77))
varm, moisture, charge, output = calculate(98, 12, 77)


########Calling function from function

def calculate(varm, moisture, charge):
    return int((varm + moisture) / charge)


calculate(90, 12, 20) * 10


def standardization(a, p):
    return a * 10 / 100 * p * p


standardization(45, 1)


def all_caltculation(varm, moisture, charge, p):
    a = calculate(varm, moisture, charge)
    b = standardization(a, p)
    print(b * 10)


all_caltculation(1, 3, 5, 10)

def all_caltculation(varm, moisture, charge, a, p):
    print(calculate(varm, moisture, charge))
    b = standardization(a, p)
    print(b * 10)


all_caltculation(1, 3, 5, 10, 9)

#########Local and Global Variables###
list_store = [1, 2]

def add_element(a, b):
    c = a * b
    list_store.append(c)
    print(list_store)

add_element(1, 9)