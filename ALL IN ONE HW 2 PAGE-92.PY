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
