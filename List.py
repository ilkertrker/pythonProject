#Lists#######

#can_change
#Can_order

notes = [1, 2, 3, 4]
type(notes)

name = ["a", "b", "c", "d",]

not_nam = [1, 2, 3, "a", "b", True, [1, 2, 3]]

not_nam[0]
not_nam[5]
not_nam[6]
not_nam[6][1]
type(not_nam[6][1])
notes[0] = 98
print(notes)
not_nam[0:4]

####List Metodology###
dir(notes)
len(notes)
len(not_nam)

#append : For add obj to the list
notes
notes.append(100)
notes

#pop : For delete obj
notes.pop(4)
notes

#insert : add at index
notes.insert(2, 99)
notes