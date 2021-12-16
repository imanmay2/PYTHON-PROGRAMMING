# # SUNDAY,MONDAY,WEDNESDAY,SATURDAY...…….n terms...
li=["SUNDAY","MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY"]
n=int(input("Enter number of terms: "))
r=0
a=0
b=1
for i in range(n):
    a=a+r
    if(a>6):
        a=a-(7*b)
        b=b+1
        
    r=r+1
    print(li[a],end=' ')

    


    


