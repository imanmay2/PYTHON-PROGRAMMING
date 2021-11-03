s=int(input("enter the first number "))
e=int(input("enter the last number of the series of the prime numbers"))
for i in range(s,e+1):
    ct=0
    for j in range(1,i+1):
        if(i%j==0):
            ct=ct+1
    if(ct==2):
        print(i)
