"""
this is question one of assignment one
entering name city and address along with major and phone number 
"""
name = input("enter your name")
print("hello", name)
#got nmae from user
address = input("can you enter your address with city and state")
zipcode = int(input("can you enter the zipcode"))
number = int(input("now can we get your phone number"))
major = input("last thing is your major")
print("address:", address)
print("zipcode:", zipcode)
print("phone number:", number)
print("major:", major)
#this get all the information needed and displays it to be checked by user

"""
this is question two of assignment one
finding how many arces they user has
"""
feet = int(input("enter how many square feet of land you own"))
acres = feet/43560
print("acres:", acres)
#user enters the feet and we divide it by one acre to see how many the user has

"""
question:3
assignment:1
distance traveled if not delays
"""
speed1 = 70
time_1 = 6
time_2 = 10
time_3 = 15
distance_1 = speed1*time_1
distance_2 = speed1*time_2
distance_3 = speed1*time_3
print("distance 1 traveled:", distance_1)
print("distance 2 traveled:", distance_2)
print("distance 3 traveled:", distance_3)
#this is set and cant be changed but shows the distance going 70 in set times 
"""
question:3
assignment:1
distance traveled if not delays
redoing not sure if i did it right 
"""
speed = int(input("enter speed in mph"))
time = int(input("enter time in hour"))
distance = speed*time
print("distance traveled:", distance)
#user enter the speed they want and time they want to see the distance
"""
question:4
assignment:1
this checks to see what age they classify as
"""
age = int(input("enter your age"))
if age <= 1 and age > 0:
    print("infant")
elif age > 1 and age < 13:
    print("child")
elif age >= 13 and age < 20:
    print("teenager")
else :
    print ("adult")
#this will decide what age the person classifys as
"""
question: 5
assignment: 1
this will make the user add up to a dollar in the cents
"""
print("have the cents add up to one dollar")
pennies = int(input("enter how many pennies you want"))
nickels = int(input("enter how many nickels you want"))
dimes = int(input("enter how many dimes you want"))
quarters = int(input("how many quarters you wnat"))
#this ask how many of each cent they would like in the to program 
total = (pennies *.01)+(nickels*.05)+(dimes*.10)+(quarters*.25)
#this will multiply the amount they enter to the cent they choose
if total == 1:
    print("perfect match")
elif total > 1:
    print("to much")
else:
    print("not enough")
#will let them know if they got the exact amount or not 
"""
question:6
assignment:1
find weather if its a leap year or not
"""
year = int(input("enter the year to check if it will leap"))
#asked to enter the year they want to see if its a leap year 
if year %4:
    print ("not leap")
else:
    print("leap!!!")
#this if stament will determine weather or not if it is a leap year or not using the mod 4
"""
question:7
assignment:1
determines the BMI of the person and then tells them about their weight
"""
height = int(input("enter your height in inches"))
weight = int(input("enter weight in pounds"))
#the user enters the weight and height 
BMI = (weight*703)/(height)
print("BMI:", BMI)
if BMI < 18.5:
    print("your underweight")
elif BMI >=18.5 and BMI <= 25:
    print("good weight")
else:
    print("over weight")
#this will determine if they are over weight under or average 
"""
question: 8
asssignment: 1
find the amount joe lost and made with the stocks
"""





