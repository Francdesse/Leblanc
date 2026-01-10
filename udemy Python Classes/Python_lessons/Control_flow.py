# 1.8.26
# COntrol Flow Mini Project:
'''
    time frame: Good Morning - 5 AM to 11 AM
    time frame: Good Afternoon - 12 PM to 17 PM
    time frame: Good Evening - 18 PM to 23 PM
    else night
'''
# time = int(input("What time of day is it? "))
# if time >= 5 and time <= 11:
#     print("Good Morning")
# elif time >= 12 and time <= 17:
#     print("Good Afternoon")
# elif time >= 18 and time <= 23:
#     print("Good Evening")
# elif time <0 or time > 23:
#     print("invalid time, try again")
# else:
#     print("Good Night")
#

'''
-----------------------------------------------------------
For loops
'''
# # range
# a = 6
# sum = 0
# # for i in range(1,a):
# #     sum=i*a
# #     print(sum,i)
# #
# # # lets do it again with a while loop
# i=1
# while i < a:
#     sum = a * i
#     i = i + 1
#     print(sum, i)

'''
-----------------------------------------------------------
Break statements
'''

# for i in range(1, 10):
#     if i == -5:
#         print("Found it!")
#         break
#     else :
#         print(i)
#     continue

'''
-----------------------------------------------------------
finding even and odd numbers
'''

for i in range(1, 10):
    if i % 2 == 0:
        print(f"{i} is even")
        continue
    else:
        print(f" {i} is odd")
    # continue
