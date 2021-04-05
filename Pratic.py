"""
print("MARKS CALCULATION")
m=int(input("Enter Math Marks"))
h=int(input("Enter Hindi Marks"))
e=int(input("Enter English Marks"))
s=int(input("Enter Science Marks"))
ss=int(input("Enter S.Science Marks"))

total=((m+h+e+s+ss))
print("Your TotalMarks is",total)
"""
"""
print("Find Biggest Value")
a=int(input("Enter 1st Value"))
b=int(input("Enter 2nd Value"))

if a>b:
    print("A is big")
else:
    print("B is big")
"""
"""
print("ODD or EVEN")
a=int(input("Enter Value"))
if a%2==0:
    print("Even")
else:
    print("ODD")
"""
"""
print("AGE Finder : ")

a=int(input("Enter Age"))
if a<18:
    print("Minor Age Person")
else:
    print("Major Age Person")
"""
"""
print("Find Leap Year")
a=int(input("Enter Year : "))
if a%4==0:
    print("Leap Year")
else:
    print("Not Leap Year")
"""
"""
print("VOTER CARD Apply")
name=input("Enter Name ")
age=int(input("Enter Age "))
if age>=18:
    print(name," can apply")
else:
    print(name," can't apply")
"""
"""
print("Find Area of Triangle")
h=int(input("Enter Height "))
b=int(input("Enter Base "))

print("Area = ",int((1/2)*b*h))
"""
"""
print("Find Area of Square ")
a=int(input("Enter side "))
print("Area = ",a*a)
"""
"""
print("Find Area of Circle ")
a=int(input("Enter Value "))
print("Area = ",(22/7)*a*a)
"""
"""
print("Find Area of Paralleogram")
h=int(input("Enter Height "))
b=int(input("Enter Base "))
print("Area = ",h*b)
"""
"""
print("Grade Checker")
m=int(input("Enter Math "))#100
h=int(input("Enter Hindi "))#100
e=int(input("Enter English "))#100
s=int(input("Enter Science "))#100
ss=int(input("Enter S.Science "))#100
sub=["Math","Hindi","English","Science","S.Science"]
marks=[m,h,e,s,ss]
for i in range(len(sub)):
    print(sub[i]," ",marks[i])
for i in range(1):
    total=int((m+h+e+s+ss)/5)
    print(total,"%")
    if total>=90:
        print("A")
    elif total>=75 and total<=89:
        print("B")
    elif total<=74 and total>=60:
        print("C")
    elif total<=59 and total>=40:
        print("D")
    elif total<33:
         print("Fali")
"""
"""
print("Company Salary")
s=int(input("Enter Salary "))
if s>=20000:
    print("A level Salary")
elif s>=15000 and s<=19999:
    print("B Level Salary")
elif s>=10000 and s<=14999:
    print("C Level Salary")
else:
    print("Basic Salary")
"""
"""
print("Table")
for i in range(1,11):
    print(f'{2*i:5}{3*i:5}{4*i:5}{5*i:5}{6*i:5}{7*i:5}{8*i:5}{9*i:5}{10*i:5}')
"""
"""
print(" Square Root")
for i in range(2,11):
    print(f'{i**2:5}{i**3:5}')
"""
"""
print(round(5.56))
print("Find Minimum Number ")
l=[5,4,87,8,6,8,4,2,3,87,12,4,5]
for i in l:
    print(i)
"""
"""
print("Basic Salary Net Salary Calculator")
bs=int(input("Enter Basic Salary "))
if bs>=10000:
    hra=int((bs/100)*5)
    da=int((bs/100)*4)
    ns=bs+hra+da
    print("NET SALARY = ",ns,"\n"+"HRA = ",hra,"\n"+"DA = ",da)
elif bs<10000 and bs>5000:
    hra=(bs/100)*6
    da=(bs/100)*5
    ns=bs+hra+da
    print("NET SALARY = ",ns,"\n"+"HRA = ",hra,"\n"+"DA = ",da)
elif bs<=5000:
    hra=400
    da=300
    ns=bs+hra+da
    print("NET SALARY = ",ns,"\n"+"HRA = ",hra,"\n"+"DA = ",da)
"""
"""
print("LOOP")
a=int(input("Enter Number "))
b=1
while(b<=a):
    print(b)
    b=b+1
"""
"""
a=int(input("Enter Number "))
b=1#start point
while(b<=a):#b is less than a is True termanete
    print(a)#print counting
    a=a-1#decrement
"""
"""
print("Table")
a=int(input("Enter Number "))
b=1#start point
while(b<=10)#terminate
    print(a*b)#a into b
    b=b+1#b is adding one
"""
"""
print("Fectorial Series")
a=int(input("Enter Number "))
b=1#start point
c=1
while(b<=a):
    c=c*b
    b=b+1
print(c)
"""
"""
print("Even Number")
num=int(input("Enter A number "))
i=2
sumE=0
sumO=0
while(i<=num):
    if i%2==0:
        print(i)
        sumE=sumE+i
    elif i%2!=0:
        sumO=sumO+i
    i=i+1
print("TOTAL EVEN =",sumE)
print("TOTAL ODD = ",sumO)
"""
print("FOR LOOP")
"""
print("Table")
num=int(input("Enter Number For Table "))
for i in range(1,11):
    print(num*i)
"""
"""
print("Counting")
num=int(input("Enter Number For Counting "))
for i in range(num):
    print(i)
"""
"""
print("FACTORIAL SERISE")
num=int(input("Enter Number "))
sum=0
t=1
for i in range(num):
    sum=t*(num-i)
    t=sum
print(t)
"""
"""
print("ODD EVEN")
num=int(input("Enter Number For Table "))
odd=0
even=0
for i in range(1,num+1):
    if i%2==0:
        print(i)
        even=even+i
    elif i%2!=0:
        odd=odd+i
print("ODD ",odd)
print("EVEN",even)
"""
"""
print("Febonice serise")
a,b=0,1
for i in range(10):
    c=a+b
    a=b
    b=c
    print(a)
"""
"""
a,b=2,3
min=a if a>b else b #if a grater than b=a else b
print(min)

a,b="hii","hello"
p=a if len(a)<len(b) else b #if a lessthan b=a else b
print(p)
"""
"""
m=[4,5,8,5,366,9,2,6,4,2,385,5] #count for back side
print(m[-3])
"""
"""
num=int(input("Enter Number "))
i=1
sum=0
"""                                #function creation
"""
def sum():
    a=int(input("Enter A number : "))
    b=int(input("Enter A number : "))
    c=a+b
    print("Total = ",c)
sum()
"""
"""
def table():
    a=int(input("Enter Number for Table : "))
    for i in range(1,11):
        print(i*a)
table()
"""
"""
def voter():
    name=input("Enter Name of Voter : ")
    age=int(input("Enter Age of Voter : "))
    if age>=18:
        print(name,"can Apply for Voter Id Card")
    else:
        print(name,"can't Apply for Voter Id Card")

voter()
"""
"""
sum=0
user=int(input("Enter A number : "))
for i in range(1,(user+1)):
    if i%2==0:
        sum=sum+i
    else:
        pass
print(sum)
"""
"""
user=int(input("Enter Number : "))
sum=0
for i in range(user):
    sum=sum+i
print(sum)
"""
"""
import time

user=int(input("Enter A number : "))
t1=time.time()
a=0
b=[*str(user)]
for i in b:
    a=a+int(i)
print(a)
t2=time.time()
print(t2-t1)

#Sum of digits

num=int(input("Ente A number : "))#1234
t3=time.time()
a=[*str(num)]
sum=0
i=0
while i<len(a):                 #i=0 len=5
    b=a[i]                      #i=1,2,3,4
    sum=sum+int(b)              #1,3,6,10
    i=int(i)+1                  #1,2,3
print(sum)
t4=time.time()
print(t4-t3)
"""
"""
def RI(p,r,t):
    t=(r*p*t)/100
    print("total Rate",t)
p=int(input("Enter Total Amount : "))
r=int(input("Enter Rate on Amount : "))
t=int(input("Enter time in year : "))
RI(p,r,t)
"""
"""
def fact(a):
    c=1
    sum=0
    for i in range(a):
        sum=c*(a-i)
        c=sum
    print("Factorial = ",c)
fact(5)
"""
"""
s="hello"
print(s[0:0])
"""
"""
#find squere
def squ(a):
    t=a*a
    print("Squre of ",a,"=",t)
squ(5)
"""
"""
#Revers The Number or String
a=int(input("Enter a Number : "))
a=str(a)
print(a[::-1])
"""
"""
#Phone Number Checkerss
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
phoneNumber = phonenumbers.parse("+918766370876") 
print(geocoder.description_for_number(phoneNumber, "en"))
Carrier = carrier.name_for_number(phoneNumber, 'en') 
print(Carrier)
"""
"""
#Password checker and decoder
import random
def p_c():
    s=input("Entre a String : ")
    s=[*s]
    b=[]
    n=1
    for i in range(10000):
        a=s
        random.shuffle(a)
        if a not in b:
            a="".join(a)
            b.append(a)
        elif a in b:
            pass
        print(n)
        n=n+1
    b=set(b)
    for i in b:
        print(i)
    print(len(b))
p_c()
"""
"""
for i in range(10):
    print(" "*i,)
    print("*"*i,end="")
    print(" "*(10-i))
    print("*"*i,end="")
for i in range(1,10):
    print("*"*(10-i))
    print(" "*i)
    print(end="")
"""
#List

#a=[1,4,5,8,9,6,4,78,5,3,9,4,32,3,1,32,77]
"""
a=[]
for i in range(5):
    u=int(input("ENTER A NUMBER : "))
    a.append(u)
#print(a)#ptint list
#print(a[0:5]) #print list elements 0 to 5
#print(a[-6:-3]) #print list elements from back side to -3 to -6
#print(a[0]==2)#check in list that 0th item is 1 or not! if a[0]=1 is true else false
#for i in a:
#    print(i)#print a list in by for loop line by line

#check that your itm is in list or not
user=int(input())
if user in a:
    print("YESS")
else:
    print("NO!")
"""
#print(len(a)) #check lenght of the list
"""
#Append a item in list
b=45
a.append(b)
print(a)
"""
"""
#Remove item for a list
a.remove(1)
print(a)
"""
"""
#Delet list items by slicing
del a[0:8]
print(a)
"""
"""
#input intger value in a list
b=[]
a=input().split(" ")
for i in a:
    b.append(int(i))
print(b)
"""
"""
a=[4,5,8,9,6,3,2,1,7,8]
nl=[]
for i in a:
    m=a.index(i)
    if m in a:
        a.remove(m)
    else:
"""
"""
a=[1,2,3,4,6,5,4,3,2,1]
for i in range(int(len(a)/2)):
    if a[i]==a.pop():
        print("SAME")
    else:
        print("Not Same")
"""
#Sets 
#a={"one","two","three","four","five"}
#print(a)

#for i in a:
#    print(i)

#print("one" in a) Check data in set

#a.add("NINE")#ADD DATA in SETS
#print(a)

#a.update(["MANGO","ORANGE","BANANA","APPLE"]) #Update data form list
#print(a)

#a={"one","two","three","four","five"}
#b={"NINE","TEN","ELEVEN"}
#print(a.union(b))#combind two sets togather
"""
#Exercise Question 2: Return a set of identical items from a given two Python set
a={1,2,5,4,7,8,96,12}
b={1,2,5,4,7,88,976,172}
c=set()#empaty set for storing data
for i in a:
    if i in b:#check that i is in b or not
        c.add(i)#append i in c
    else:
        pass #pass the value 
print(c)
"""
"""
#Exercise Question 3: Returns a new set with all items from both sets by removing duplicates
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
a=set1.union(set2)#add two set togather and print unique items
print(a)
"""
"""
#Exercise Question 4: Given two Python sets, update first set with items that exist only in the first set and not in the second set.
a={10,20,30}
b={20,40,50}
c=set()
for i in a:
    if i not in b:
        c.add(i)
    else:
        pass
print(c)
"""
"""
#Exercise Question 5: Remove 10, 20, 30 elements from a following set at once
set1 = {10, 20, 30, 40, 50}
set2=set()
for i in :
    if i != 10 and 20 and 30:
        set2.add(i)
#set1.clear()
#set1=set2
print(set2)
"""
"""
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

diff =set2.difference(set1)
print(diff)
"""
"""
set1 = {10, 20, 30, 40, 50}
set1.discard(20)#it remove element form set
print(set1)
"""
"""
set1 = {10, 20, 30, 40, 50}
set2 = {100, 200, 300, 400, 500}
a=set1.isdisjoint(set2)#it print False if any element exist in both sets else print True
print(a)
"""
"""
set1 = {10, 20, 30, 40, 50}
set2 = {100, 200, 300, 400, 500}
set1.symmetric_difference_update(set2)#if any element present in both sets do it will remove the element and commbind the set togather update a set1
print(set1)
"""
"""
a={1,2,3,4}
print(type(a))
"""
"""
a=[5,5,6,7,7,7]
b=set(a)
def test(Ist):
    if Ist in b:
        return 1
    else:
        return 0
for i in filter(test,a):
    print(i,end="")
"""
"""
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1=(set1^set2)# it retuen those elements which is once present in a both setd like ==> {10,20,60,70}
print(set1)
"""
"""
a=[1,4,7,8,5,6]
print(min(a))
"""
"""
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
a=set1.copy()
a.remove(10)
print(a)
"""
"""
import pywhatkit as kt#it change a image into Assic Values like @#$%^&* els.
kt.image_to_ascii_art("seg.jpg","IMAGES.txt")#first neet to write origanel imahe name and than write image name which you want to creat
"""
#Dictionary
"""
#Q1
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
for i in dic1,dic2,dic3:#it will Add all given dictonary togather in a dic1
    dic1.update(i)#here wwe will update data into a dic1 and make a singel dict
print(dic1)#print a dic1 output #{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""
"""
#Tkinter Basic Window
from tkinter import * 
root = Tk()
root.geometry("300x300")
root.title("Ashu First Program")
test = Label(root, text="Welcome",font=("arial",16,"bold")) 
test.pack()
root.mainloop() 
"""
#Below are the two lists convert it into the dictionary
"""
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
a={}
for i in range(len(keys)):
    a[keys[i]]=values[i]
print(a)
"""
"""
#Merge following two Python dictionaries into one
a={'Ten': 10, 'Twenty': 20, 'Thirty': 30}
b={'ELEVEN': 11, 'NINE': 9, 'SIX': 6}
for i in a,b:
    b.update(i)
print(b)
"""
"""
#Access the value of key ‘history’ from the below dict
sampleDict = { 
   "class":{
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

print(sampleDict["class"]["student"]["marks"]["history"])
"""
"""
family={"child1":{"name":"PAWAN","age":20,"work":{"HOME WORK"}},
        "child2":{"name":"Rahul","age":21},
        "child3":{"name":"Ashu","age":19}
print(family["child1"])
"""
"""
#Use dictionary to store antonyms of words. E.g.- 'Right':'Left', 'Up':'Down', etc. Display all words and then ask user to enter a word and display antonym of it.
antonym={"left":"right","right":"left","up":"down","down":"up"}
for i in antonym.keys():
    print(i)
user=input("Enter String for Antonym : ")
print("Antomny of ",user,"is ",antonym[user])
"""
"""
key_value={}
key_value[2] = '64'       
key_value[1] = '69'
key_value[4] = '23'
key_value[5] = '65'
key_value[6] = '34'
key_value[3] = '76'
print(sorted(key_value.keys()))
"""
"""
#short dictionary using keys of them
key_value={}
key_value[2] = '64'       
key_value[1] = '69'
key_value[4] = '23'
key_value[5] = '65'
key_value[6] = '34'
key_value[3] = '76'

for i in sorted(key_value):
    print(f"({i},{key_value[i]})",end="")
"""
"""
#need to access key using value
key_value={}
key_value[2] = '64'       
key_value[1] = '69'
key_value[4] = '23'
key_value[5] = '65'
key_value[6] = '34'
key_value[3] = '76'
for i in sorted(key_value.values()):
    print(key_value)
"""
"""
#Check list item is same or not
a=[1,2,56,4]
b=[1,2,56,4]
print(a==b)
"""
"""
#print two marge dictionary value togather
a={1:1,2:1,3:1}
b={4:1,6:1,8:1}
for i in a,b:
    b.update(i)
value=b.values()
sum=0
for i in value:
    sum=sum+i
print(sum)
"""     
#TEST 21-3-2021
"""
#CHECk WHICH VALUE IS BIGGER
a=int(input("ENTER A VALUE : "))
b=int(input("ENTER B VALUE : "))
c=int(input("ENTER C VALUE : "))
if a>b and a>c:
    print("A IS BIGGER!")
elif b>a and b>c:
    print("B IS BIGGER!")
else:
    print("C IS BIGGER!")
"""
"""
#Calculation Program
print("1 for +","\n"+"2 for -","\n"+"3 for *","\n"+"4 for /")

cal=int(input("ENTER CALCULATION TYPE : "))
v1=int(input("Enter 1st value :"))
v2=int(input("Enter 2nd value :"))

if cal==1:
    print(v1+v2)
elif cal==2:
    print(v1-v2)
elif cal==3:
    print(v1*v2)
elif cal==4:
    print(int(v1/v2))
"""
"""
#salary Class
salary=int(input("Enter Salary : "))
if salary>1 and salary<1000:
    print("Poor Class")
elif salary>1001 and salary<2000:
    print("Medium Class")
elif salary>2001:
    print("Rich Class")
"""
"""
user_value=int(input("Enter A Value : "))
if user_value % 2==0:
    print("Even Number ")
else:
    print("Odd Number")
"""
"""
#New collection 

import collections
a=collections.deque

a.append(25)
a.append(2)
a.append(22)
a.append(28)

print(a.popleft())
print(a)
"""
"""
#check position of element in list
list1=[]
import random
for i in range(30):
    a=random.randint(1,100)
    list1.append(a)
print(list1)
inde=int(input("Enter a Number for checking Position : "))
print(list1.index(inde))
"""
"""
#remove all duplicater elemet form list
list1=[]
list2=[]
import random
for i in range(30):
    a=random.randint(1,100)
    list1.append(a)
print(list1)
for i in list1:
    if i not in list2:
        list2.append(i) 
print(list2)
"""
"""
#Make saprate list of negetive and positive elements
list1=[]
p=[]
n=[]
import random
for i in range(30):
    a=random.randint(-100,100)
    list1.append(a)
print(list1)
for i in list1:
    if i>=0:
        p.append(i)
    else:
        n.append(i)
print("Positive List : ",p)
print("Negetive : ",n)
"""
"""
#change into upper case
list1=["ashu","pawan","monu","rahul","sunil"]
for i in list1:
    i=i.upper()
    print(i)
"""
"""
#Celsius into Fahrenheit
temp=[25,78,96,36,100,47,52]#Celcis
for i in temp:
    f=(i*9/5)+32
    print(f,"Fahrenheit")
"""
"""
#print madian value form list without touching other value
a=[1,4,8,5,9,6,3,1,8,2,3,7,45]
m=int(len(a)/2)
print(m)
print(a[m])
"""
"""
#print number of negetive and positive elements in list
list1=[]
p=0
n=0
import random
for i in range(20):
    a=random.randint(-100,100)
    list1.append(a)
print(list1)
for i in list1:
    if i>=0:
        p=p+1
    else:
        n=n+1
print("Positive List : ",p)
print("Negetive : ",n)
"""
"""
a=set()
b=set()
s={"ashu","aman","bggggg","sdv","bopdf","asgjhfdbnvb","byertfyuew"}
for i in s:
    print(i)
    if i.startswith("a"):
        a.add(i)
    elif i.startswith("b"):
        b.add(i)
print(a)
print(b)
"""
#Tuple 

"""
tuple1=("Aata","Daal","Roti","Sabji","Rice")
#Access Tuple Data
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])

# Negative Access Tuple Data
print(tuple1[-3])
print(tuple1[-1])
print(tuple1[-2])

#Access Tuple Data using Range
print(tuple1[0:5:2])

# Negative Access Tuple Data using range
print(tuple1[0],"\n")

#Access Tuple Data usingLoop
print("Len")
for i in range(len(tuple1)):
    print(tuple1[i])

print("\n"+"Direct")
for i in tuple1:
    print(i)

#check item is in tuple
print("Rice" in tuple1)

#Add Tuples togather
a=(1,2,4,5,7,8)
b=(2,3,6,9,8,5,7,4)
c=a+b
print(c)

#Remove Tuple using del function
b=(2,3,6,9,8,5,7,4)
del b
#print(b)

#Check Adding element in Tuple
#Error
b=(2,3,6,9,8,5,7,4)
b[5]=6
"""
"""
a=int(input("Enter : "))
b=0
c=a
sum=0
while a>b:
    sum=a*c-a
    c=sum
    a=a-1
    b=b+1
print(c)
"""
#File Handling

f=open("text.txt","r")

"""
#1. Write a function in python to read the content from a text file "poem.txt" line by line and display the same on screen.


for i in f:
    print(i,end="")
"""
"""
#Write a function in python to count the number of lines from a text file "story.txt" which is not starting with an alphabet "T". 

num=0
for i in f:
    if (i.startswith("T"))==True:
        num=num+1
    else:
        pass
print(num)
"""
"""
#print(f.readline())#print first line of file

num=int(input("Enter A Number : "))
i=2
while (i<=num):
    if num%2==0:
        print("EVEN :",num)
    else:
        print("ODD : ",num)
    num=num-1

"""
"""
num=(input("Enter A Number : "))
num=[*num]
sum=0
for i in num:
    sum=sum+int(i)
print(sum)
"""
"""
def sod(num):
    a=num
    num=str(num)
    num=[*num]
    sum=0
    for i in num:
        sum=sum+int(i)
    print("Total : ",sum)

    sum=0
    while(a!=0):
        b=a%10
        sum=sum+b
        a=a/10
    print(int(sum))
sod(123)
"""
def count_word(Data):
    
    num=0
    for i in Data:
        if i!=" ":
            num=num+1
        else:
            pass
    print("Total Character : ",num)
a=f.readlines()
count_word(a)








