# Datatyoes:
# list
# turple
# dictionary

##### List

"""
List Datatype:
1. it is just a consecutive collection of related items/ words
2. represent a group of values as a single entity, order is very important
3. it allows duplicated values as well
4. it is represented by a square bracket []
5. value are seperated by a comma
EX:

Note:
    list can have duplicate values
    list is mutable(we can append the list(meaning adding more items to the list))

"""
a = [1,2,5,9, 9.9]
b = [9,6,8, 9.9]
# print(a[:])
# print(a[:3])
# print(a[2:6])

# adding new items to the list
# a.extend([2,5,7])
# print(a)
# a.sort()
# print(a)

#repeating list
# print(a*2)
# print(a+b)
# print(min([a]))

"""
Dictionary:
key and value pair
    1. key - numbers, string, tuple
    2. value - python objects
    EX:
"""
# d1 = {
#     "name": "testing",
#     "age": 20,
#     "workplace": "healthcare",
#     "location": "remotely"
#     }
# print(f"my name is {d1['name']}, I am {d1['age']} years old, I work in {d1['workplace']} {d1['location']}")

#Example of dictionary with a list
d2 = {
    "cars": ["tesla","ford", "nissan"],
    "price": [100000, 200000, 300000],
    "color": "red"
    }
print(d2["cars"] [2])