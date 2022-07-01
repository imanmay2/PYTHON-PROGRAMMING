# ..........INPUT A WELCOME MESSAGE............
print(".............WELCOME.............")

# ......INPUT THREE NUMBERS AND DISPLAY THE LARGEST AND THE SMALLEST ONE......
n1=int(input("enter the number"))
n2=int(input("Enter the second number"))
n3=int(input("Enter the third number"))
print("Largest Number is",max(n1,n2,n3))
print("smallest Number is",min(n1,n2,n3))

'''
*
**
***
****
*****
'''
n=int(input("enter the range of the series"))
for i in range(1,n+1):
    print("*"*i)

'''
12345
1234
123
12
1
'''
n=int(input("enter the number"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

'''
A
AB
ABC
ABCD
ABCDE
'''
n=int(input("enter the range of the pattern"))
for i in range(1,n+1):
    a=65
    for j in range(1,i+1):
        print(chr(a),end=' ')
        a=a+1
    print()

#print the sum ::::     1+x+x**2.........x**n
x=int(input("enter the number"))
n=int(input("enter the range"))
s=0
for i in range(0,n+1):
    s+=x**i
print("sum of the series is",s)

# print the sum::::::     1-x+x**2-.........x**n
x=int(input("enter the number"))
n=int(input("Enter the range"))
s=0
for i in range(0,n+1):
    if(i%2==0):
        s+=x**i
    else:
        s-=x**i
print("The sum of the series is",s)

# print the sum::::::   x+((x**2)/2)-.........(x**n)/n
n=int(input("enter the range  of the series"))
x=int(input("enter the number"))
s=x
for i in range(2,n+1):
    if(i%2==0):
        s+=(x**i)/i
    else:
        s-=(x**i)/i
print("The sum of the sereis is",s)

# print the series::::::    x+(x**2)/2!-(x**3)/3!+........(x**n)/n!
n=int(input("enter the range  of the series"))
x=int(input("enter the number"))
s=x
f=1
for i in range(2,n+1):
    f=f*i
    if(i%2==0):
        s+=(x**i)/f
    else:
        s-=(x**i)/f
print("The sum of the sereis is",s)

# DETERMINE WHETHER THE NUMBER ENTERED IS PERFECT NUMBER, ARMSTRONG NUMBER OR A PALINDROME NUMBER.
n=int(input("enter the number"))

                #PERFECT NUMBER.......
per=n
s=0
for i in range(1,per):
    if(per%i==0):
        s=s+i
if(s==per):
    print("........IT'S A PERFECT NUMBER........")
else:
    print("NOT A PERFECT NUMBER")

                # ARSTRONG NUMBER........ 
arm=n
s=0
while(arm!=0):
    r=arm%10
    s=s+(r**3)
    arm=arm//10
if(n==s):
    print("........IT'S A ARMSTRONG NUMBER........")
else:
    print("Not a armstrong number")

            #PALINDROME NUMBER........
pal=n
rev=0
while(pal!=0):
    r1=n%10
    rev=(rev*10)+r
    pal=pal//10
if(rev==n):
    print(".........IT'S A PALINDROME NUMBER........")
else:
    print("Not a palindrome number")


# ACCEPT A NUMBER AND PRINT WHTHER IT'S A PRIME OR COMPOSITE.
n=int(input("enter the number you want to enter"))
ct=0
for i in range(1,n):
    if(n%i==0):
        ct+=1
if(ct==1):
    print("........IT'S A PRIME NUMBER........")
else:
    print("........IT'S A COMPOSITE NUMBER........")

#DISPLAY THE TERMS OF FIBBONACCI SERIES....
a=0
b=1
n=int(input("enter the terms"))
print("The fibbonacci series is")
print(a)
print(b)
for i in range(3,n+1):
    c=a+b
    print(c)
    a=b
    b=c

# COMPUTE THE H.C.F AND L.C.M OF MINIMUM TWO INTEGER NUMBERS.
x=int(input("enter the first number"))
y=int(input("enter the second number"))
hcf=0
lcm=0
for i in range(1,x+1):
    if(x%i==0 and y%i==0):
        hcf=i
lcm=(x*y)/hcf
print("........THE H.C.F AND L.C.M IS........",hcf,lcm)


#COUNT THE DISPLAY THE THE NUMBER OF VOWELS, CONONANTS,UPPERCASE,LOWERCASE CHARACTERS IN A STRING.

str1=input("enter the string you want to enter")
v=0
up=0
lo=0
conso=0
for i in str1:
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U"):
        v+=1
    else:
        conso+=1
for j in str1:
    if(j.isupper()):
        up+=1
    elif(j.islower()):
        lo+=1
print("COUNT OF UPPERCASE IS",up)
print("COUNT OF LOWERCASE IS",lo)
print("COUNT OF VOWEL IS",v)
print("COUNT OF CONSONANTS IS",conso-1)


#DETERMINE WHETHER THE INPUT STRING IS PALINDROME OR NOT.
str1=input("Enter the string you want to enter")
if(str1==str1[::-1]):
    print("........IT'S A PALINDROME STRING........")
else:
    print("not a palindrome string ")

# find the largest and smallest of the list/tuple.
n=eval(input("enter the number in list/tuple"))
print("........MAXIMUM NUMBER........",max(n))
print("........MINIMUM NUMBER........",min(n))

# INPUT A LIST AND SWAP THE ELEMNTS FROM THE EVEN POSITION TO IT'S CORRESPONDING ODD POSITIONS
li=eval(input("enter the list"))
if(len(li)%2!=0):
    s-=1
for i in range(0,len(li),2):
    li[i],li[i+1]=li[i+1],li[i]
print("........LIST AFTER SWAPPiNG IS........",li)

# INPUT A LIST/TUPLE THAT SEARCHES A ELEMENT FROM A LIST
li=eval(input("enter the list/tuple"))
n=eval(input("enter the element to be serached"))
if(n in li):
    print("........YES FOUND IN THE LIST/TUPLE..........")
else:
    print(".........NOT FOUND IN THE LIST/TUPLE........")


# CREATE A DICTIONARY WITH ROLL NUMBER, NAME AND MARKS OF N STUDENTS AND DISPLAY THE NAME WHOSE HAS SECURED MORE THAN 75 MARKS.
n=int(input("enter the number of students"))
d={}
for i in range(n):
    r=int(input("Enter the roll number of the student"))
    n=input("enter the name of the student")
    m=float(input("enter the marks of the student"))
    d[r]=[n,m]
for i in d:
    if(d[i][1]>75):
        print(d[i][0])
