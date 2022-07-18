# To compute the value of pi upto 'n' decimal terms entered by the user.
n=int(input("enter the range of the value of pi: "))
pi="3.142857"
d="142857"*n
if(n<=6):
    print(pi[0:n+2])
elif(n>6):
    print(pi+d[0:n-6])
        
    

