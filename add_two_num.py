# add to numbers
# from math import remainder


# a = 32
# b = 5

# # print("The sum of a and b is ", a + b)

# # print("The remainder when a is divided by b is ", a % b)

# # print(a < b)
# # print(a == b)

# a = input("enter first number: ")
# b = input("enter second number: ")
# a = int(a)
# b = int(b)
# avg = (a + b)/2
# print("The average if a and b is", avg)

# -------------------------------------------------

# a = 40
# b = "Nilam's" # need to use " " so you can able to ' if you need
# # print(a + b)  # not going to work because both types are diff
# print(a, b)
# print(type(a))
# print(type(b))

# greeting = "Good Morning, "
# name = "Nilam"
# # print(type(name))
# # print(greeting + name) # or
# c = (greeting + name)
# print(c)
# print(name[3])  # name[3] = "D" <-- Does not work
# print(name[0:3])  # index 3 not going to print it will print up to index two
# print(name[1:4])  # it will print from index one to index 3
# # ^^^ its called slicing of string mean taking the thing you wanted only and its work same name[:3]
# print(name[-1])  # - start counting from back of the string

name = "GoodMornningNilam"
d = name[0::2]  # will print every other string index its call skip value
print(d)

story = "Once upon a time there was a yputuber named XYZ who uploaded. \n python \t course"

#  String Functions
# print(len(story))
# print(story.endswith("course"))  # is the story end with course
# print(story.count("a"))  # how many a in stroy
# # if the first later is not capitalize the will make capital
# print(story.capitalize())
# print(story.find("python")) #give the index no for first occurrence
# Will replace all xyz occurrence if you more then one
print(story.replace("XYZ", "NILAM"))
print(story)  # \n were ever you write it will replace from their new line in sequences when you wants to print tab you can add \t
