'''
-----------------------------------------------------------
1.11.26
'''
# list
#
# emp = ['Mark', 33, 'Manager']
# comp = ['Apple', '123 ave', 'NY']
# comp[2] = 'CA' #upding the list
#
# print(f'my name is {emp[0]}, I am {emp[1]} years old working as a {emp[2]}\
#  I currently work at {comp[0]} in {comp[2]} located at {comp[1]}')
#
# # to append is to add something new to the list
# comp.append('HR')
# print(f'my name is {emp[0]}, I am {emp[1]} years old working as a {emp[2]}\
#  I currently work at {comp[0]} in {comp[2]} located at {comp[1]}.\
#  I would glady refer you to my {comp[3]} department')
#
# comp.remove('HR') #to remove something from the list/
# print(comp)

# Dictionary

client = {
            "name": input("Enter your name: "),
            "age": int(input("Enter your age: ")),
            "job": input("Enter your job title: ")
}
print(client)
del client["age"]
print(client)