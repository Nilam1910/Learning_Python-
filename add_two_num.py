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

# name = "GoodMornningNilam"
# d = name[0::2]  # will print every other string index its call skip value
# print(d)

# story = "Once upon a time there was a you tuber named XYZ who uploaded. \n python \t course"
#                                                                     **************
#  String Functions
# print(len(story))
# print(story.endswith("course"))  # is the story end with course
# print(story.count("a"))  # how many a in stroy
# # if the first later is not capitalize the will make capital
# print(story.capitalize())
# print(story.find("python")) #give the index no for first occurrence
# Will replace all xyz occurrence if you more then one
# print(story.replace("XYZ", "NILAM"))
# print(story)  # \n were ever you write it will replace from their new line in sequences when you wants to print tab you can add \t
# _________________________________________Dictionary___________________

# myHome = {
#     "city": "Joliet",
#     "state": "IL",
#     "population": "147323",
#     "houseNO": [1500, 11400, 1300, 1200, 1100]
# }

# # Dictionary Methods

# print(list(myHome.keys()))  # prints the keys of the dictionary myHome
# print(myHome.values())  # Prints the values of the dictionary
# # Prints the keys and values of the dictionary(mean all contents of dictionary)
# print(myHome.items())

# updateDict = {
#     "Nina": "Friend",
#     "population": "150000"  # you can update exciting values also
# }

# # updates the dictionary by adding key-value pairs from updateDict
# myHome.update(updateDict)
# print(myHome)
# print(myHome.get("Nina"))  # Print value associated with key "Nina"
# print(myHome["Nina"])


########################### Set ##############


a = {}
# print(type(a))  # this one make empty dictionary

# b = set()  # set is non repeatable,
# print(type(b))
# # adding value to an empty set
# b.add(4)
# print(b)
# b.add(5)
# print(b)
# b.add(5)  # cannot added repeatedly
# # b.add([1, 2, 3]) # cannot add list or dictionary to sets
# b.add((1, 2, 3,))  # tuple can be added
# b.remove(4)  # its removable
# print(b)

# print(len(b))  # print the length of set
# ---homework---------------------------------???????
# check out following methods
# pop()
# clear()
# Union()
# intersection()

myHome_things = {
    "Pankha": "Fan",
    "Dabba": "Box",
    "Kela": "Banana",
    "Saeb": "Apple",
}

# print("Options are ", myHome_things.keys())
# a = input("Enter the Hindi Word\n")
# print("The meaning of your word is:", myHome_things[a])
# # this will not give you error but will say non it the word is not their
# print("The meaning of your word is:", myHome_things.get(a))

unique = set  # when you see unique word that mean think bout set

# num1 = int(input("Enter number 1\n"))
# num2 = int(input("Enter number 2\n"))
# num3 = int(input("Enter number 3\n"))
# num4 = int(input("Enter number 4\n"))
# num5 = int(input("Enter number 5\n"))

# s = {num1, num2, num3, num4, num5}
# print(s)  # it will print only unique no, even tho you add same nos and it goes up to 5 time then print all the no you have added

# s = {18, "18", 18.1, 18}
# s = {18, 18.0, "18"}  # it will give you only 2 because in set 18 nad 18.0 is same
# print(s)
# print(len(s))
# s = {} # this is not a empty set its a dictionary, set() is empty set
# print(type(s))

# favLang = {}
# a = input("ENter your favorite language Nina\n ")
# b = input("ENter your favorite language Bina\n ")
# c = input("ENter your favorite language Tina\n ")
# d = input("ENter your favorite language Ama\n ")
# favLang["Nina"] = a
# favLang["Bina"] = b
# favLang["Tina"] = c
# favLang["ama"] = d

# In python language we don't use semicolen
# print(favLang)  # this will print all inputs ( value can be same )
# hashable means you cannot able to change the value changing
# in set list cant come and tuple can come bit tuple means not changeable

# -------------if-elif-else ladder in python
# a = 33

# if (a < 3):  # any one can be true once its true its stop executing further
#     print("The value of a is greater then 3")
# elif (a > 11):
#     print("The value of a is greater then 11")
# elif (a > 17):
#     print("The value of ais greater then 17")
# elif (a < 17):
#     print("The value of ais less then 17")
# else:
#     print("The value is not greater then 11 ir 17")

# --- you can write as many as if they are separate from each other only attached with elif and else they are to gather

# a = 22
# if (a > 9):
#     print("greater")
# else:
#     print("less then")

# age = int(input("enter your age: "))

# if age > 18:
#     print("Yes")
# else:
#     print("No")

# -------- operators-----------------
# = is assign operator, == is as equal

# age = int(input("Enter your age: "))
# if (age > 34 and age < 53):
#     print("you can work with us")
# else:
#     print("you can not work with us")

# ----------- percentage -------------------
# sub1 = int(input("Enter first subject marks\n"))
# sub2 = int(input("Enter first subject marks\n"))
# sub3 = int(input("Enter first subject marks\n"))

# if (sub1 < 33 or sub2 < 33 or sub3 < 33):
#     print("You are fail")
# elif (sub1+sub2+sub3)/3 < 40:
#     print("yoy are fail")
# else:
#     print("Congratulations! you are passed the exam")

# ------------- spam --------------------------
# text = input("Enter the text\n")

# if("make a lot of money" in text):
#    spam = True
# elif("buy now" in text):
#    spam = True
# elif("click this" in text):
#    spam = True
# elif("subscribe" in text):
#    spam = True
# e
#    spam = False

# if(spam):
#    print("This text is spam")
# else:
#    print("This text is not spam")

# --------- Given username length -----------
# write a program to find whether a given username contains less then 10 characters or not
# username = input(("Enter the username\n "))
# if (len(username) < 10):
#     print("Yes")
# else:
#     print("No")

# --------- Given name is present ---------
# names = ["nina", "tina", "amanda", "amy", "arati"]
# name = input("Enter the name to check\n")

# if name in names:
#     print("Your name is present")
# else:
#     print("Your name is not present")

# ------------ Calculate the Garde ---------------
marks = int(input("Enter your "))

if marks > 90:
    grade = "Ex"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"
print(f"Your grade is {grade}")
# print("Your grade is " + grade) # or you can write this way
