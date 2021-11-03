print("the following 4 digit numbers are the tech numbers")
for i in range(1000,10000):
    a=(i%10)        #5
    b=(i//10)%10    #2
    c=(i//100)%10   #0
    d=(i//1000)%10  #3
    s=d*10+c
    s1=b*10+a
    sum=s+s1
    pro=sum**2
    if(pro==i):
        print(i)
        
