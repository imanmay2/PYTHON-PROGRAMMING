#wap to input friends name and phone number and do create a dictionary.. and do delete update, etc, etc...
n=int(input("enter how many friends??"))
fr={}
for i in range(n):
    key=input("enter the name of your friend")
    value=int(input("enter the phone number of your friend"))
    fr[key]=value
print("....MENU....")
print("1. DISPLAY FRIENDS DICTIONARY")
print("2. ADD NEW FRIENDS")
print("3. DELETE A PARTICULAR FRIENDS DETAILS")
print("4. MODIFY ANY PHONE NUMBER OF YOUR FRIEND")
print("5. CHECK IF ANY ONE OF YOUR FRIEND IS PRESENT OR NOT")
print("6. DISPLAY FRIENDS DICTIONARY IN SORTED MANNER")
print("7. EXIT")
ans="yes"
while(ans=="yes"):
    choice=int(input("enter your choice...."))
    if(choice==1):
        print("..........FRIENDS DICTIONARY IS .........")
        print(fr)
    elif(choice==2):
        n1=int(input("How many friends do you want to add"))
        for i in range(n1):
            k=input("enter the name of your friend")
            v=int(input("enter the phone number of your friend"))
            fr[k]=v
        print(".....MODIFIED DICTIONARY IS....")
        print(fr)
    elif(choice==3):
        f=input("enter the friends name to be removed")
        if(f in fr.keys()):
            del fr[f]
            print("...UPDATED DICTIONARY IS...")
            print(fr)
        else:
            print("No such friends name is found..")
    elif(choice==4):
        f1=input("enter the friends name to modifY the phone number")
        if(f1 in fr.keys()):
            fr[f1]=int(input("Enter the phone number you want to modify"))
            print("...UPDATED DICTIONARY IS...")
            print(fr)
        else:
            print("No such friends name is found..")
    elif(choice==5):
        f2=input("enter the friends name")
        if(f2 in fr.keys()):
            print("YES",f2,"IS PRESENT IN THE DICTIONARY")
        else:
            print("YES",f2,"IS PRESENT IN THE DICTIONARY")
    elif(choice==6):
        print("......FRIENDS NAME IN SORTED MANNER IS AS FOLLOWS......")
        print(sorted(fr))
    else:
        break
    ans=input("want to continue").lower()
    
            
