#1. WAP that prompts for a phone number of 10 digits and two dashes, with the dashes after the area code and the next three numbers.
# For e.g 017-555-1212 is a valid input.
str1=input("Enter the number")
if(str1[3]=='-' and str1[7]=='-' and len(str1[0:3])==3 and len(str1[4:7])==3 and len(str1[8:len(str1)])==4):
    print("VALID INPUT!!!!")
else:
    print("NOT A VALID INPUT!!!!")


#3. WAP accept two lists and display the sum of their individual index's elements.
# For e.g L=[3,1,4] and M=[1,5,9] ......RESULTS SHOULD BE R=[4,6,13]
li1=eval(input("ENTER THE LIST 1: "))
li2=eval(input("ENTER THE LIST 2: "))
li3=[]
if(len(li1)!=len(li2)):
    print("ERROR FOUND!!!! ENTER TWO LISTS WITH SAME LENGTH")
else:
    for i in range(len(li1)):
        s=0
        s=li1[i]+li2[i]
        li3.append(s)
    print("LIST 3 IS AS FOLLOWS",li3)


# 4. WAP THAT ROTATES THE ELEMENTS IN A LIST.THAT IS FIRST ELEMENT GOES TO THE SECOND, SECOND GOES TO THE THIRD .....AND LAST ELEMENT GOES TO THE FIRST.
li=eval(input("ENTER THE LIST  YOU WANT: "))
li.insert(0,li.pop(len(li)-1))
print(li)


#5. WAP TO PRINT THE LONGEST WORDS FROM THE LIST OF WORDS.
str1=input("ENTER THE SENTENCE: ")
li1=[]
li=str1.split()
for i in li:
    ct=0
    for j in i:
        ct=ct+1
    li1.append(ct)
print("MAXIMUM WORD PRESENT IN THE LIST OF THE WORDS IS AS FOLLOWS",li[li1.index(max(li1))])


#6 .WAP THAT WILL CREATE A LIST OF NUMBERS CONTAINING NUMBER FROM 1 TO 99 WHICH ARE THE MULTIPLES OF 3 OR 5.
li=[]
for i in range(1,100):
    if(i%3==0 or i%5==0):
        li.append(i)
print("THE LIST IS AS FOLLOWS", li)
