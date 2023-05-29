# Compute the sum of digits in all numbers from 1 to n. When a function gets a number n, find the sum of digits in all numbers from 1 to n.
# Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15
#O(n)
n=5
result=0
while n>0:
    sum = 0+n
    result = result+n
    n= n-1
    print('the sum is', sum)
    print(result)

#so Since its says sum I know for sure that it would me need to be adding instead of mulplying. Once I figured that part
#then the next challenge was to come up with the 15. first I figure out the decrement then after couple then find a way
#to get the incremental of adding to get to 15 then voila

# Find the max number from 3 values.
# Example: 124, 21, 32. Result = 124.
#O(logn)
n= 0
if n>0 and n < 50:
    print('number displayd in the min range', n)
elif n>=50 and n<100:
    print('number entered is in the midrange', n)
elif n>=100:
    print('number is in the max range', n)
else:
    print('enter a different number', n)
#So as soon that I saw max number from 3 values, I automatically thought of if else statements with 3 ranges of numbers
# a min, mid, and max and thats how I came up with my answer

# Count odd and even numbers. Count odd and even digits of the whole number.
# Example: number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).

#O(1)
numb_list = [3,4,5,6,0]
for numb in numb_list:
    if (numb %2==0):
        print('even number ', numb)
    elif (numb %2):
         print('add number ', numb)

# When I first read it, I thought I was support to count even numbers and odd numbers but the example showed otherwise.
# so I automatically thought of a number list but figuring out how to take the number out was the challenge
