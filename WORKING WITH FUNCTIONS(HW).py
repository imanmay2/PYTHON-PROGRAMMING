# 23.. to create 3 different functions and print the and print the highest one as per the Q.
def compare_int(n1,n2):
    if(n1>n2):
        print("GREATER IS : ",n1)
    elif(n2>n1):
        print("GREATER IS : ",n2)
def compare_chr(ch1,ch2):
    if(int(ch1)>int(ch2)):
        print("GREATER IS : ",ch1)
    elif(int(ch2)>int(ch1)):
        print("GREATER IS : ",ch2)
def compare_string(str1,str2):
    if(len(str1)>len(str2)):
        print("GREATER IS : ",str1)
    elif(len(str2)>len(str1)):
        print("GREATER IS : ",str2)
compare_int(int(input("ENTER THE NUMBER 1 : ")),int(input("ENTER THE NUMBER 2: ")))
compare_chr(input("ENTER THE CHARACTER 1 : "),input("ENTER THE  CHARACTER 2: "))
compare_int(input("ENTER THE STRING 1 : "),input("ENTER THE STRING 2: "))   


# 24.. to create a function named polygon of 3 different types.and do the following operation as per the Q.
def poly_sq(n,ch):
    for i in range(n):
        print(ch*n)
def poly_rec(x,y):
    for i in range(x):
        print("@"*y)
def poly_tri():
    n=int(input("ENTER THE LENGTH OF THE TRIANGLE : "))
    for i in range(1,n+1):
        print("*"*i)
poly_sq(int(input("ENTER THE SIDE OF THAT POLYGON : ")),input("ENTER THE CHARACTER TO BE PRINTED"))
poly_rec(int(input("ENTER THE LENGTH : ")),int(input("ENTER THE BREADTH : ")))
poly_tri()