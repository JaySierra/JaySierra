"""
author: Jay Sierra
assignment: 3
Question: 4
this code finds the make and model of cars and the year and it will and breake
the speed as well as display it
"""
class car:
    def __init__(self, year_model, make, speed):
        self.year_model = year_model
        self.make = make
        self.speed = speed

    def accelerate(self):
        print(self.speed + 5)

    def brake(self):
        print(self.speed - 5)

    def get_speed(self):
        print(speed)





year_model = int(input("enter year model:"))
make = input("name if car:")
speed = int(input("enter speed:"))
car1 = car(year_model, make, speed)


start = 0 
while start == 0:
    option = int(input("one accelerate, two brake, three speed check"))
    if option == 1:
        car1.accelerate()
    elif option == 2:
        car1.brake()
    elif option == 3:
        car1.get_speed()
    else:
        print("nothing was entered")
    start = int(input("0 to go again anything else for nothing"))
"""
author: Jay SIerra
asssignemnt: 3
Question: 2
this code will have the user enter their id and it will access there information
"""
class employee:
    def __init__(self,ID_number):
        self.ID_number = ID_number
        
    def SusanMeyers(self):
        print("hello susan meyers.", "ID:",self.ID_number,"department: accounting.",
                  "job title: vice president")
    def MarkJones(self):
        print("hello Mark Jones.", "ID:", self.ID_number,
              "department: IT.", "job title: programmer")
    def JoyRogers(self):
        print("hello Joy Rogers.", "ID:", self.ID_number,
              "department: manufacturing.","job title: engineer")



ID_number = int(input("enter ID number"))
person = employee(ID_number)


if(ID_number == 47899):
    person.SusanMeyers()
elif(ID_number == 39119):
    person.MarkJones()
elif(ID_number == 81774):
    person.JoyRogers()
else:
    print("nothing was entered right")

"""
author: jay sierra
assignment:3
question:3
this code will be using a class and it will have user input there name and combine it and
make them an email with it.
"""
class employees:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def fullname(self):
        print(self.first_name,self.last_name)

    def EMAIL(self):
        print(self.first_name.lower(),".",self.last_name.lower(),self.email)


first_name = input("enter your first name:")
last_name = input("enter your last name:")
email = input("enter email domain include the @:")
person = employees(first_name, last_name, email)

person.fullname()
person.EMAIL()

"""
author: Jay Sierra
assignment: 3
question: 4
this code will get all 25 students and total point of all 6 courses and then
divides it by 600 to find the precent of each students and sort there precent and averages it all
"""
class s:
    def __init__(self, c1, c2, c3, c4, c5, c6):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4
        self.c5 = c5
        self.c6 = c6

    def precent(self):
        print((self.c1 + self.c2 + self.c3 + self.c4 + self.c5 + self.c6)/600)

    def setto(self):
        a1 = []
        a1.append(self.c1)
        print(a1)
        



print("precents:")
s1 = s(85,75,65,100,20,55)
s1.precent()

s2 = s(95,75,85,65,55,100)
s2.precent()

s3 = s(25,45,85,65,78,20)
s3.precent()

s4 = s(95,99,98,95,96,97)
s4.precent()

s5 = s(45,52,65,75,85,95)
s5.precent()

s6 = s(48,54,23,65,84,78)
s6.precent()

s7 = s(78,15,20,0,25,32)
s7.precent()

s8 = s(98,92,91,25,20,10)
s8.precent()

s9 = s(47,59,26,12,15,15)
s9.precent()

s10 = s(15,65,2,15,25,15)
s10.precent()

s11 = s(100,100,100,100,95,62)
s11.precent()

s12 = s(12,54,56,98,15,59)
s12.precent()

s13 = s(15,48,75,59,26,32)
s13.precent()

s14 = s(69,58,47,41,52,63)
s14.precent()

s15 = s(78,45,12,89,65,32)
s15.precent()

s16 = s(48,51,20,59,62,30)
s16.precent()

s17 = s(68,53,10,42,57,68)
s17.precent()

s18 = s(45,23,89,45,58,69)
s18.precent()

s19 = s(48,59,26,20,15,48)
s19.precent()

s20 = s(98,97,95,69,92,20)
s20.precent()

s21 = s(85,74,85,96,85,96)
s21.precent()

s22 = s(84,95,62,32,14,52)
s22.precent()

s23 = s(84,95,62,96,98,95)
s23.precent()

s24 = s(20,25,63,85,95,74)
s24.precent()

s25 = s(78,45,12,89,56,99)
s25.precent()

print("sorted list:")
newlist = [0.66,0.79,0.53,0.96,0.69,0.58,0.28,0.56,0.29,0.22,0.92,0.49,0.42,0.55,
           0.53,0.45,0.49,0.54,0.36,0.78,0.86,0.56,0.88,0.60,0.63]
for _ in range(len(newlist)):
    for i in range(len(newlist)-1):
        if newlist[i]>newlist[i+1]:
            newlist[i],newlist[i+1]=newlist[i+1],newlist[i]
print(newlist)

print("average:")
a1 =(85+95+25+95+45+48+78+98+47+15+100+12+15+69+78+48+68+45+48+98+85+84+20+78)/25
a2 =(75+75+45+99+52+54+15+92+59+65+100+54+48+58+45+51+53+23+59+97+74+95+95+25+45)/25
a3 =(65+85+85+98+65+23+20+91+26+2+100+56+75+47+12+20+10+89+26+95+85+62+62+63+12)/25
a4 =(100+65+65+95+75+65+0+25+12+15+100+98+59+41+89+59+42+45+20+69+96+32+96+85+89)/25
a5 =(20+55+78+96+85+84+25+20+15+25+95+15+26+52+65+62+57+58+15+92+85+14+98+95+56)/25
a6 =(55+100+20+97+95+78+32+10+15+62+59+32+63+32+30+68+69+48+20+96+52+95+74+99)/25
print("average for class one:",a1)
print("average for class two:",a2)
print("average for class three:",a3)
print("average for class four:",a4)
print("average for class five:",a5)
print("average for class six:",a6)




