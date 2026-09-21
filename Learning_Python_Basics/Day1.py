# a,b,c = 1,2,"test"
# print(f'were testing something {a}, {b}, and {c}')
#
# #List: uses []
# test = [1,2,"test", 9]
#
# print(test) #printing the whole list
# test.insert(3, "new") #another way of adding a value to the list, but you can pick where you want to add it
# print(test)
#
# test.append("Bird") #add item at the end of the list
# print(test)
#
# del test[0] # remove item from the list
# print(test)

#Tuple: uses () - are immutable which means you cannot change them

#Dictionary: uses {} - are mutable which means you can change them

# stu = {"First name": "John", "Last name": "Doe", "Grade": 9, "Class": "Algebra"}
# # print(stu)
# # print(stu["First name"],stu["Grade"])

# #Simple way to write
# stu = {}
# stu["FirstName"] = "John"
# stu["LastName"] = "Doe"
# stu["Grade"] = 9
# stu["Class"] = "Algebra"
# print(stu)


# #Control Statement
# name = input("Enter your name: ")
# if name == "Jose":
#     print(f"Hello, {name}! How is your day going so far?")
# else:
#     print(f'Have a great day {name}!')
#

# #For Loops
# for i in range(5+1):
#     if i % 2 == 0:
#         print(i, "even")
#     else:
#         print(i, "odd")

sum1 = 0
for j in range(5+1):
    sum1 = (sum1 + j)
    print(j, sum1)