#Checking for the smith number.e.g :: 666 is a smith number....where sum of the
#digit is equal to the individual prime factors...also count the repeated one..too

def sum1(n):
    su=0
    while(n!=0):
        r=n%10
        su=su+r
        n=n//10
    return su
        
n=int(input("Enter the number: "))
t=n
k=n
e=sum1(n)
print("Sum of the digits of the number is: ",e)

#Caclculating the prime factors..
li_fact=[]
d=2
l=n//2
while(d<l):
    if(n%d==0):
        li_fact.append(d)
        n=n/d
        d=2
    else:
        d+=1
# finding the sum of the individual digit's number of the list
s2=0
for i in li_fact:
    s2+=sum1(i)
if(e==s2):
    print("SMITH NUMBER")
else:
    print("NOT A SMITH NUMBER")

        
    
