#wap to take a input an check whether the entered value is present or not in the dictionary..

dic={0:"Zero",1:"One",2:"Two",3:"Three",4:"Four"}
ans="yes"
while(ans=="yes"):
    val=input("enter the value").capitalize()
    print("You have entered the value",val)
    for i in dic:
        if(dic[i]==val):
            f=1
            break
    if(f==1):
        print(val,"exists in the existing dictionary")
    else:
        print("no found in the dictionary")
    ans=input("want to input the value again????")
    
    

