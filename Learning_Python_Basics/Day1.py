a,b,c = 1,2,"test"
print(f'were testing something {a}, {b}, and {c}')

#List: uses []
test = [1,2,"test", 9]

print(test) #printing the whole list
test.insert(3, "new") #another way of adding a value to the list, but you can pick where you want to add it
print(test)

test.append("Bird") #add item at the end of the list
print(test)

del test[0] # remove item from the list
print(test)