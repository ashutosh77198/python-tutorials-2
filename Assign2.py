#QUES1
"""
x="Python is a great language!", said Fred. "I don't ever remember
having this much fun before."
print(x)
"""
#QUES 2
"""
year=int(input("Enter year to be checked:"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("The year is a leap year!")
else:
    print("The year isn't a leap year!")
"""

#QUES3
"""
list=[]
extraid=[]
eid=[]
new=[]
x=input("Enter a number to use in a lopp")
for i in range(int(x)):
    b=input("enter a string")
    list.append(b)
    extraid.append(id(list[i]))
print(list)
print(extraid)
list.sort()
for j in list:
    print(j)
    eid.append(id(j[i]))
    new.append(j)
print(eid)
print(new)
"""
"""
student_tuples = [
    ('Ashutosh', 'kumar', 24),
    ('saroj', 'ghimire', 20),
    ('nirmal', 'karki', 58),
    ('karun', 'karki', 29)

]

b=sorted(student_tuples, key=lambda student: student[2])
student_tuples.sort(key=lambda student: student[2])#unnecessary
print(b)
print(student_tuples)
"""

#ques 6
"""
list1=["ashutosh", "verma", "shrestha","john"]
if "john" in list1:
    print("Found")
else:
    print("not found")
"""

#QUES 7
"""
age=0
tuples = [
    ('Ashutosh', 'kumar', 24),
    ('saroj', 'ghimire', 18),
    ('nirmal', 'karki', None),
    ('karun', 'karki', 99)]
new = []
for val in tuples:
    if val[2] != None :
        new.append(val)
print(new)

for i in new:
    age=i[2]+ age

finalavg=age/len(new)
print(finalavg)

for j in new:
    if finalavg < j[2]:
        print(j[0] + " " +"is OLD")
    else:
        print(j[0] + " " +"is YOUNG")
"""
#QUES 8
"""
def is_prime(ranum):
    if ranum > 1:
        for i in range(2,ranum):
            if ranum % i == 0:
                print(ranum, "It is a  not a prime number and FALSE")
                break
        else:
            print(ranum, "It is a prime number and TRUE")
    else:
        print(ranum, "It is not a prime number and False")


is_prime(int(input("Enter a number")))
"""
#QUES 9
"""
def binary_search(arr, low, high, x):

    if high >= low:

        mid = (high + low) // 2


        if arr[mid] == x:
            return mid


        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)


        else:
            return binary_search(arr, mid + 1, high, x)

    else:

        return -1


# Test array
arr = [7, 8, 11, 15, 2]
x = 10


result = binary_search(arr, 0, len(arr) - 1, x)

if result != -1:
    print("It is present at index", word(result))
else:
    print("It is not present in array")
"""
#QUES 10
"""
def change_case(word):
    initial = [word[0].lower()]
    b=[]
    print(word[1:])
    for c in word[1:]:
         if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            initial.append('_')


            initial.append(c.lower())

         else:
            initial.append(c)


    return  ''.join(initial)
word = "ThisIsCamelCased"
print(change_case(word))
"""
#QUES 11
"""
import os
print (os.path.splitext("README.txt")[1])

filename = input("Input the Filename: ")
extension = filename.split(".")
print(extension)
print ("The extension of the file is : " + extension[0])
"""
#QUES 13 and 14
"""

def include(entry,entry2):
        fileInfo=entry
        fileInfo2 = entry2
        csvfile=open('fileInfo.csv','w',newline='')
        csvfile2 = open('fileInfo2.csv', 'w', newline='')
        object=csv.writer(csvfile)

        for row in fileInfo:
                object.writerow(row)
                print(object)
        csvfile.close()
        fields = list(fileInfo2[0].keys())
        object2 = csv.DictWriter(csvfile2, fieldnames=fields)
        object2.writeheader()
        object2.writerows(fileInfo2)
        csvfile2.close()

include([('Name', 'Address', 'age'),('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)],[{'name': 'George', 'address': '4312 Abbey Road', 'age': 22}, {'name':
'John', 'address': '54 Love Ave', 'age': 21}])
"""

#QUES 15
"""
class Person:

    def __init__(self, Firstname, surname, address, telephone, email,account):
        self.name = Firstname
        self.surname = surname
        self.address = address
        self.telephone = telephone
        self.email = email
        self.accountno= account
    def account(self):
            print("acccount number is",self.accountno)

person = Person(
    "Saroj",
    "Ghimire",
    "kalanki12, kathmandu",
    "9801905420",
    "saroj.ghimire@example.com",
    "10180018383881"
)
print(person.name)
print(person.email)
print(person.account())
"""
#QUES 17
"""
num1= int(input("enter a number"))
num2= int(input("enter a  second number"))
oper=input("enter a operator you want to use ")
print(type(oper))
if oper=="+":
        sum=num1+num2
        print("The sum of two numbers is ",sum)
elif oper=="-":
        sub=num1-num2
        print("The substraction of two numbers is ",sub)
elif oper=="*":
        multi=num1*num2
        print("The multiplication of two numbers is ",multi)
elif oper=="/":
        if num2==0:
                next=int(input ("Please enter another number because dividing with 0 can cause undefined errors"))


        div=num1/next
        print("The division of two numbers is ",div)
"""
#QUES18
"""
class py_solution:
   def is_valid_parenthese(self, string):
        stack, char = [], {"(": ")", "{": "}", "[": "]"}

        for paren in string:
            if paren in char:
                stack.append(paren)

            elif len(stack) == 0 or char[stack.pop()] != paren:
                return False
        return len(stack) == 0

print(py_solution().is_valid_parenthese("(){}[]"))
print(py_solution().is_valid_parenthese("{)}"))
#print(py_solution().is_valid_parenthese("()"))
"""
#ques 20
"""
def extarxt(A, arr_size, sum):
    # Fix the first element as A[i]
    for i in range(0, arr_size - 2):

        # Fix the second element as A[j]
        for j in range(i + 1, arr_size - 1):

            # Now look for the third number
            for k in range(j + 1, arr_size):
                if A[i] + A[j] + A[k] == sum:
                    print("Triplet is", A[i],
                          ", ", A[j], ", ", A[k])


    # If we reach here, then no
    # triplet was found
    return print("yes")


# Driver program to test above function
A =[-25, -10, -7, -3, 2, 4, 8, 10]
sum = 0
arr_size = len(A)
extarxt(A, arr_size, sum)
"""
#ques 18
"""
import json
with open('user.json','w') as file:
         json.dump({
            "name": "Ashutosh Verma",
            "age": 24,
            "friends": ["niraml","saroj"],
            "balance": 35.80,
            "other_names":("babul","rahul"),
            "active":True,
            "spouse":None
        }, file, sort_keys=True, indent=4)

with open('user.json', 'r') as file:
        user_data = json.load(file)
print(user_data)
"""
