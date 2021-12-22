# # SUNDAY,MONDAY,WEDNESDAY,SATURDAY...…….n terms...
li=["SUNDAY","MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY"]
n=int(input("Enter number of terms: "))
a=0
r=0
b=1
for i in range(n):
    if a==21:
        a,r,b=0,0,1
    a=a+r
    r=r+1
    if(a<=6):
        print(li[a])
    else:
        print(li[a-7*b])
        b+=1
print("..........................The End..................")
   
    

    


    


