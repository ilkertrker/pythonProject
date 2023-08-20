################
#Interview Question
#################

#Purpose : Write a fuction for change sentences which writing below.

# before: "hi my name is john and i am learning python"
# after: "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"

len("test123000")
range(len("test123000"))

range(0, 5)

for i in range(len("test123000")):
    print(i)

4 / 2 == 0
4 % 2 == 0


def alternating(string):
    new_string = ""
    # looking for index
        for string_index in range(len(string)):
            #if index is odd make it upper
            if string_index % 2 == 0:
                new_string += string[string_index].upper()
            #if index is not odd make it lower
            else:
                new_string += string[string_index].lower()
        print(new_string)


alternating("Please check it for test")


