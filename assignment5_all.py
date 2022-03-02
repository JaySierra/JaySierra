"""
author: Jay sierra
assignment:5
question:1
date: 3/1/2022
discription:this code will make all the strings and numbers into morse code
"""
s = input("enter whatever to make morse code")
for ch in s:
    if ch == '0':
        print("-----")
    elif ch == '1':
        print(".----")
    elif ch == '2':
        print("..---")
    elif ch == '3':
        print("...--")
    elif ch == '4':
        print("....-")
    elif ch == '5':
        print(".....")
    elif ch == '6':
        print("-....")
    elif ch == '7':
        print("--...")
    elif ch == '8':
        print("---..")
    elif ch == '9':
        print("----.")
    elif ch == 'a' or ch == 'A':
        print(".-")
    elif ch == 'b' or ch == 'B':
        print("-...")
    elif ch == 'c' or ch == 'C':
        print("-.-.")
    elif ch == 'd' or ch == 'D':
        print("-..")
    elif ch == 'e' or ch == 'e':
        print(".")
    elif ch == 'f' or ch == 'F':
        print("..-.")
    elif ch == 'g' or ch == 'G':
        print("--.")
    elif ch == 'h' or ch == 'H':
        print("....")
    elif ch == 'i' or ch == 'I':
        print("..")
    elif ch == 'j' or ch == 'J':
        print(".---")
    elif ch == 'k' or ch == 'K':
        print("-.-")
    elif ch == 'l' or ch == 'L':
        print(".-..")
    elif ch == 'm' or ch == 'M':
        print("--")
    elif ch == 'n' or ch == 'N':
        print("-.")
    elif ch == 'o' or ch == 'O':
        print("---")
    elif ch == 'p' or ch == 'P':
        print(".--.")
    elif ch == 'q' or ch == 'Q':
        print("--.-")
    elif ch == 'r' or ch == 'R':
        print(".-.")
    elif ch == 's' or ch == 'S':
        print("...")
    elif ch == 't' or ch == 'T':
        print("-")
    elif ch == 'u' or ch == 'U':
        print("..-")
    elif ch == 'v' or ch == 'V':
        print("...-")
    elif ch == 'w' or ch == 'W':
        print(".--")
    elif ch == 'x' or ch == 'X':
        print("-..-")
    elif ch == 'y' or ch == 'Y':
        print("-.-")
    elif ch == 'z' or ch == 'Z':
        print("--..")
    elif ch == ',':
        print("--..--")
    elif ch == '.':
        print(".-.-.-")
    elif ch == '?':
        print("..--..")
    else:
        print(" ")

print("\n")

"""
author: Jay sierra
assignment:5
question:2
date: 3/1/2022
discription:this code will find the number of vowel and consanants 
"""
vowel = 0
consonant = 0
letters = input("enter the word your sentence you would like")
for ch in letters:
    if ch == 'A' or ch == 'a':
        vowel += 1
    elif ch == 'E' or ch == 'e':
        vowel += 1
    elif ch == 'I' or ch == 'i':
        vowel += 1
    elif ch == 'O' or ch == 'o':
        vowel += 1
    elif ch == 'U' or ch == 'u':
        vowel += 1
    else:
        print(" ")
print("number of vowels:", vowel)
for ch in letters:
    if ch == 'B' or ch == 'b':
        consonant += 1
    elif ch == 'C' or ch == 'c':
        consonant += 1
    elif ch == 'D' or ch == 'd':
        consonant += 1
    elif ch == 'F' or ch == 'f':
        consonant += 1
    elif ch == 'G' or ch == 'g':
        consonant += 1
    elif ch == 'J' or ch == 'j':
        consonant += 1
    elif ch == 'K' or ch == 'k':
        consonant += 1
    elif ch == 'L' or ch == 'l':
        consonant += 1
    elif ch == 'M' or ch == 'm':
        consonant += 1
    elif ch == 'N' or ch == 'n':
        consonant += 1
    elif ch == 'P' or ch == 'p':
        consonant += 1
    elif ch == 'Q' or ch == 'q':
        consonant += 1
    elif ch == 'S' or ch == 's':
        consonant += 1
    elif ch == 'T' or ch == 't':
        consonant += 1
    elif ch == 'V' or ch == 'v':
        consonant += 1
    elif ch == 'X' or ch == 'x':
        consonant += 1
    elif ch == 'Z' or ch == 'z':
        consonant += 1
    elif ch == 'H' or ch == 'h':
        consonant += 1
    elif ch == 'R' or ch == 'r':
        consonant += 1
    elif ch == 'W' or ch == 'w':
        consonant += 1
    elif ch == 'Y' or ch == 'y':
        consonant += 1
    else:
        print("")
print("number of consonants:", consonant)


print("\n")

"""
author: Jay sierra
assignment:5
question:3
date: 3/1/2022
discription:this code shows us how to remove and edit strings 
"""
string1 = "P@#yn26at^&i5ve"
count = 0
for ch in string1:
    if ch == '0':
        count += 1
    elif ch == '1':
        count += 1
    elif ch == '2':
        count += 1
    elif ch == '3':
        count += 1
    elif ch == '4':
        count += 1
    elif ch == '5':
        count += 1
    elif ch == '6':
        count += 1
    elif ch == '7':
        count += 1
    elif ch == '8':
        count += 1
    elif ch == '9':
        count += 1
    elif ch == 'a' or ch == 'A':
        count += 1
    elif ch == 'b' or ch == 'B':
        count += 1
    elif ch == 'c' or ch == 'C':
        count += 1
    elif ch == 'd' or ch == 'D':
        count += 1
    elif ch == 'e' or ch == 'e':
        count += 1
    elif ch == 'f' or ch == 'F':
        count += 1
    elif ch == 'g' or ch == 'G':
        count += 1
    elif ch == 'h' or ch == 'H':
        count += 1
    elif ch == 'i' or ch == 'I':
        count += 1
    elif ch == 'j' or ch == 'J':
        count += 1
    elif ch == 'k' or ch == 'K':
        count += 1
    elif ch == 'l' or ch == 'L':
        count += 1
    elif ch == 'm' or ch == 'M':
        count += 1
    elif ch == 'n' or ch == 'N':
        count += 1
    elif ch == 'o' or ch == 'O':
        count += 1
    elif ch == 'p' or ch == 'P':
        count += 1
    elif ch == 'q' or ch == 'Q':
        count += 1
    elif ch == 'r' or ch == 'R':
        count += 1
    elif ch == 's' or ch == 'S':
        count += 1
    elif ch == 't' or ch == 'T':
        count += 1
    elif ch == 'u' or ch == 'U':
        count += 1
    elif ch == 'v' or ch == 'V':
        count += 1
    elif ch == 'w' or ch == 'W':
        count += 1
    elif ch == 'x' or ch == 'X':
        count += 1
    elif ch == 'y' or ch == 'Y':
        count += 1
    elif ch == 'z' or ch == 'Z':
        count += 1
    elif ch == ',':
        count += 1
    elif ch == '.':
        count += 1
    elif ch == '?':
        count += 1
    elif ch == '!':
        count += 1
    elif ch == '@':
        count += 1
    elif ch == '#':
        count += 1
    elif ch == '$':
        count += 1
    elif ch == '%':
        count += 1
    elif ch == '^':
        count += 1
    elif ch == '&':
        count += 1
    elif ch == '*':
        count += 1
    else:
        print(" ")
print(string1)
print("count is: ", count)
print("\n")


string2 = "/*jon is @developer & musician"
print(string2)
removed = string2[2:9]
removed1 = string2[10:20]
removed3 = string2[21:30]
newstring = removed+removed1+removed3
print("new string is:")
print(newstring)
print("\n")


string3 ="Emma-is-a-data-scientist"
print(string3)
n1 = string3[0:4]
n2 = string3[5:7]
n3 = string3[8:9]
n4 = string3[10:14]
n5 = string3[15:24]
ns = n1+" "+n2+" "+n3+" "+n4+" "+n5
print("new string is")
print(ns)
print("\n")

string4 ="hello, have a good day"
print(string4)
c1 = string4[1:2]
c2 = string4[4:5]
c3 = string4[8:9]
c4 = string4[10:11]
c5 = string4[12:13]
c6 = string4[15:17]
c7 = string4[20:22]
cs = c1+c2+c3+c4+c5+c6+c7
print("consonants are:")
print(cs)


print("\n")

"""
author: Jay sierra
assignment:5
question:4
date: 3/1/2022
discription:this code will have to user enter numbers and then it will find the
mean and average and diveation and we test out the try and excpection
"""
total = 0
inlist = []
for i in range(0,10):
    number = int(input("enter a number"))
    inlist.append(number)
    total = total + number
print(inlist)
average = total / 10
inlist.sort()
n = len(inlist)
gs = sum(inlist)
mean = gs/n
print(mean)
deviation = 2**(gs/(len(inlist)-1))
print(deviation)
nl = []
n2 = []
try:
    nl = inlist.copy()
    for i in len(nl):
        n2.append(i)
    print(n2)
except Exception as e:
    print(Exception)
finally:
    print(nl)

print("\n")

"""
author: Jay sierra
assignment:5
question:5
date: 3/1/2022
discription:this code we find out how to manipulate strings using loops 
"""
ms = "this is the string for the class"
if ms == ms:
    new = ms.title()
    print(new)
else:
    print("nothing")

remove = [" "]
for ch in remove:
    ms1 = new.replace(ch,"")
print(ms1)

ms2 = ms.title()
new_char = ["s"]
for ch in new_char:
    ms2 = ms.replace(ch,"$")
print(ms2)

ms3 = ms
for ch in ms3:
    if ms3[0] == 't':
        m3 = ms3[0].upper()

print(ms3)
