#1.WAP TO CHECK WHETHER THE VARIABLE IS ZERO NEGATIVE OR POSITIIVE.
def check(x):
    if(x<0):
        print(x,"is a negative number")
    elif(x>0):
        print(x,"is a positive number")
    else:
        print(x,"is a nuetral number")
n=int(input("Enter any number: "))
check(n)

#2.WAP that returns True if the input number is an even number , False otherwise.
n=int(input("Enter any number: "))
if(n%2==0):
    print("TRUE")
else:
    print("FALSE")
    
