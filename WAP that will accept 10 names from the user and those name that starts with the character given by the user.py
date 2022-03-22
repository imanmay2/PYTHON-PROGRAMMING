#wap that will accept 10 names from the user and display those names that starts with the character
#entered by the user.
li=eval(input("Enter the names of 10"))
n=input("Enter the character that will be print those names from the list of 10")
for i in li:
    if(i[0]==n):
        print(i)