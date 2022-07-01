import time
user1="manmay"
pass1="25082004"
username=input("Enter your username")
password=input("Enter your password")
i=0 
while(username!=user1 and password!=pass1):
    username=input("MATCH NOT FOUND ENTER YOUR USERNAME AGAIN!!!!!")
    password=input("MATCH NOT FOUND ENTER YOUR USERNAME AGAIN!!!!!")
    i=i+1
    if(i==3):
        time.sleep(4)
        i=0
    elif(username==user1 and password==pass1):
        print("MATCHED FOUND YOU CAN MOVE FORWARD")
        break



