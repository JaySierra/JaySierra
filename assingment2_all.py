"""
author: Jay Sierra
assignment: 2
question:1
i am using a loop to organize the * in a patteren  
"""
left_right = int(input("enter 1 for left or 2 for right"))
if left_right == 1:
    for row in range(0,5):
        if row ==0:
            print("*")
        elif row ==1:
            print("**")
        elif row ==2:
            print("***")
        elif row ==3:
            print("****")
        elif row ==4:
            print ("*****")
else:
    for row in range(0,5):
        if row ==0:
            print("    *")
        elif row ==1:
            print("   **")
        elif row ==2:
            print("  ***")
        elif row ==3:
            print(" ****")
        elif row ==4:
            print ("*****")
print("\n")



"""
author: Jay Sierra
assignment: 2
question:2
i am take two inputs from the user an ddoing the math for the two numbers they have entered 
"""
n = int(input("enter in the first number"))
r = int(input("enter in the second number"))
math = int(input("enter 1 to do math"))
option = 0
total = 0
while math == 1:
    option=int(input("enter 1 for math 1 or 2 for math 2"))
    if option == 1:
        total=n/r*(n-r)
    elif option == 2:
        total=n/(n-r)
    else:
        print("you didnt enter a value")
    print(total)
    math = int(input("enter one again or zero to end"))
print("\n")



"""
author: Jay Sierra
assignment: 2
question:3
i am using a loop in order to sort all the numbers in the list from least to greatest 
"""
list_a = [20,68,41,88,16,40,65,97,85]
for _ in range(len(list_a)):
    for i in range(len(list_a)-1):
        if list_a[i]>list_a[i+1]:
            list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
print(list_a)
            
print("\n")



"""
author: Jay Sierra
assignment: 2
question:4
i made my own list then i find the total of all sums of even odds and the total of all numbers 
"""
a = [1,2,3,4,5,6,7,8,9,10]
total_sum = 0
total_even = 0
total_odd = 0
for i in range(len(a)):
    total_sum = total_sum + i
for j in range(len(a)):
    if j%2==0:
        total_even = total_even + j
for p in range(len(a)):
    if p%2!=0:
        total_odd = total_odd + p
print("this is the list:", a)
print("this total sum:", total_sum)
print("this is total even:", total_even)
print("this is total odd:", total_odd)
print("\n")



"""
Author: Jay Sierra
assignment: 2
question:5
i am finding all the prime numbers between 2 - 50
"""
a = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,
     25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,
     45,46,47,48,49,50]
prime = []
for i in a :
    n = 0
    for j in range(1, i):
        if i %j == 0:
            n+=1
    if n==1:
        prime.append(i)
print(prime)

print("\n")



"""
Author: Jay Sierra 
assignment: 2
question:6 part 1
making a function for question one
"""

def left_to_right():
    for row in range(0,5):
        if row ==0:
            print("*")
        elif row ==1:
            print("**")
        elif row ==2:
            print("***")
        elif row ==3:
            print("****")
        elif row ==4:
            print ("*****")
def right_to_left():
    for row in range(0,5):
        if row ==0:
            print("    *")
        elif row ==1:
            print("   **")
        elif row ==2:
            print("  ***")
        elif row ==3:
            print(" ****")
        elif row ==4:
            print ("*****")

start = int(input("enter 0 to start"))
while start == 0:
    a = int(input("enter 1 for left or 2 for right"))
    if a == 1:
        left_to_right()
    elif a == 2:
        right_to_left()
    else:
        print("no value entered")
    start = int(input("enter zero again to go again if not enter any number"))

print("you have ended the while loop")
print("\n")



"""
assignment: 2
question:6 part 2
making a function for question two inputs 
"""
def math_1():
    total=n/r*(n-r)
    print(total)

def math_2():
    total=n/(n-r)
    print(total)
    


math = int(input("enter 1 to do math"))
option = 0
total = 0
while math == 1:
    n = int(input("enter in the first number"))
    r = int(input("enter in the second number"))
    option=int(input("enter 1 for math 1 or 2 for math 2"))
    if option == 1:
        math_1()
    elif option == 2:
        math_2()
    else:
        print("you didnt enter a value")
    math = int(input("enter one again or zero to end"))
print("you have ended the loop")
print("\n")



"""
assignment: 2
question:6 part 3
making a function for question three 
"""
def list_order():
    list_a = [20,68,41,88,16,40,65,97,85]
    for _ in range(len(list_a)):
        for i in range(len(list_a)-1):
            if list_a[i]>list_a[i+1]:
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
    print(list_a)

call = int(input("enter 1 for list order or random to skip"))
if call == 1:
    list_order()
else:
    print("you have skipped")

