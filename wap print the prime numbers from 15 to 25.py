print("the prime numbers are")
for i in range(15,26):
    ct=0
    for j in range(1,i+1):
        if(i%j==0):
            ct=ct+1
    if(ct==2):
        print(i,end=' ')
    
