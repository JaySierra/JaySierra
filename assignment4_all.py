"""
author: Jay SIerra
assignment: 4
question: 1
date:2/25/2022
discription: this will make a dictenary and it will add remove and make new objects inside
"""
es = dict({1:"susan",2:"accounting",3:"vice president",
           4:"mark",5:"IT",6:"programmer"
           ,7:"joy",8:"manufacturing",9:"engineer"})
    
ID = int(input("enter the 4 digit code"))
while ID != 2020:
    print("incorect input")
    ID = int(input("enter the 4 digit code"))

if(ID == 2020):
    do = int(input("1 look employee,2 add emplyee,3 delete employee,4 change name and departemnt, 4 quit"))
    if do == 1:
        print(es)
    elif do == 2:
        add = es.iteams()
    elif do == 3:
        key = int(input("1 susan 2 mark 3 joy"))
        if key == 1:
            del es[1]
        elif key == 2:
            del es[4]
        elif key == 3:
            del es[7]
        else:
            print("didnt enter anything")
    else:
        print("didnt enter anything")
else:
    print("all done")
print("\n")

"""
author:jay sierra
assignment: 4
question:2
date:2/28/2022
discription:this code will have the user enter in 20 number then sort it in a list
then it will find the total and then the average.
"""
total = 0
cool = []
for i in range(0,20):
    number = int(input("enter a number"))
    cool.append(number)
    total = total + number
print(cool)
cool.sort()
print("this is sorted list")
print(cool)
print("total is: ", total)
average = total / 20
print("average: ", average)
print("\n")

"""
author:Jay sierra
assignment:4
question:3
date:2/28/2022
discription:this code will ask teh user to see what key they want and when entered they
will see what that key is multipied by itself 
"""
my_dict = {'one' : '1*1',
           'two' : '2*2',
           'three' : '3*3',
           'four' : '4*4',
           'five' : '5*5'
           }
for key, value in my_dict.items():
     print(key, value)
key = input("enter a number 1-5")
if key in my_dict:
    print(my_dict['one'])
elif key in my_dict:
    print(my_dict['two'])
elif key in my_dict:
    print(my_dict['three'])
elif key in my_dict:
    print(my_dict['four'])
elif key in my_dict:
    print(my_dict['five'])
else:
    print("nothing")
print("\n")


"""
author:Jay sierra
assignment:4
question:4
date:2/28/2022
discription:this code gets random numbers from the range of 1-20
then it finds the secind largest number in the list and then it makes a new list removing
the repeated numbers 
"""
from random import seed
from random import randint

seed(1)

biglist = []
for _ in range(100):
	value = randint(0, 20)
	biglist.append(value)
largest = 0
print(biglist)
for i in range(0,len(biglist)):
    if i>0 and i!=20:
        largest = i
    else:
        print(largest)
newbig = []
for i in biglist:
    if i not in newbig:
        newbig.append(i)
print("removed repeated numbers")
print(newbig)

        

