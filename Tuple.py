#############
### Tuple###

#unchangebla
#inorder

t = ("perk", "mark",1 ,2 )
type(t)

t[0]
t[0:3]

t = list(t)
t[0] = 99
t = tuple(t)
t
type(t)

####Set####

#Changeable
#unorder
######If you need speed , you can use SET

#difference()

set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

#what are the difference about set1 and set2
set1.difference(set2)
set2.difference(set1)
set1 - set2

#what is sum of two
#symetric_difference()
set1.symmetric_difference(set2)
set2.symmetric_difference(set1)

#instersection two set

set1.intersection(set2)
set2.intersection(set1)
set1 & set2

#union() sum of two set
set1.union(set2)
set2.union(set1)

#isdisjoint() or .issubset Answer is True or False
set1.isdisjoint(set2)
set2.isdisjoint(set1)

set1.issubset(set2)
set2.issubset(set1)


total = 3.4 + 2.6
print(total)

a = 9 ** (1/2)
b = 10 / 5
a-b