"""
author: Jay SIerra
date:3/8/2022
assignment:6
question:1
discription:in this code i was using regular expression in order to find all special characters
in teh file and then i put them in an object and made a new file with all the classes
"""
import re 
class student():
    def __init__(self,fn,ln,email,allc):
        self.fn = fn
        self.ln = ln
        self.email = email
        self.allc = allc

lastnames = 'Random|Kate|Alpha|Heart|Chappel|Talor|Realtor|Anorak|Worker|Project'
email = []
first = []
last = []
allcourses = []

def main():
    infile = open('stud.txt','r')
    file_contents = infile.read()
    find_email = re.findall('[a-z]+@islander.tamucc.edu',file_contents)
    email.append(find_email)
    firstname = re.findall('\n([A-Z]+[a-z]+[a-z])',file_contents)
    first.append(firstname)
    lastname = re.findall(lastnames,file_contents)
    last.append(lastname)
    allgrades = re.findall('[1-9]+[0-9]+',file_contents)
    allcourses.append(allgrades)
    infile.close()
    print(file_contents)
    print(email)
    print(first)
    print(last)
    print(allcourses)   


    ap = open('newstuds.txt','a')
    for ch in email:
        ap.write(ch)
    ap.close()

    file = open('newstuds.txt','r')
    filec = file.read()
    file.close()
    print(filec)



main()






"""
author: Jay SIerra
date:3/8/2022
assignment:6
question:2
discription:in this code i was supposed to find all errors and made the file with teh
the final sample code and make it exacly like it 
"""
import re
f1 = []
f2 = []
f3 = []
def main():
    infile = open('finalsample.txt','r')
    filess = infile.read()
    infile.close()
    

    f11 = open('f1.txt','r')
    filesss = f11.read()
    f123 = re.findall('\w[a-zA-Z0-9]+[a-zA-Z0-9]',filesss)
    f1.append(f123)
    f11.close()
    

    f11 = open('f2.txt','r')
    filessss = f11.read()
    f1234 = re.findall('\w[a-zA-Z0-9]+[a-zA-Z0-9]',filessss)
    f1.append(f1234)
    f11.close()
    

    f11 = open('f3.txt','r')
    filessss = f11.read()
    f12345 = re.findall('\w[a-zA-Z0-9]+[a-zA-Z0-9]',filessss)
    f1.append(f12345)
    f11.close()
    

    

main()


print(f1)
