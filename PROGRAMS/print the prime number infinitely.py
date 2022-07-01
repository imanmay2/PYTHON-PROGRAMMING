num=1
while(num!=0):
    ct=0
    for i in range(1,num+1):
        if(num%i==0):
            ct=ct+1
    if(ct==2):
        print(num)
    num=num+1
