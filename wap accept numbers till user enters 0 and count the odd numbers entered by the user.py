#wap accept no. till enter 0 count the number of odd number entered by the user
ct=0
while(1):
    n=int(input("emter the number"))
    if(n==0):
        break
    else:
        if(n%2!=0):
            ct=ct+1
print("the count of the odd number",ct)
