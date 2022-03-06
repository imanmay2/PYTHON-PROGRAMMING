def Nearest_Prime(n):
    a=n
    m=n
    while(1):
        ct=0
        a=a+1
        for i in range(1,a+1):
            if(a%i==0):
                ct+=1
        if(ct==2):
            break
    while(1):
        ct=0
        m=m-1
        for j in range(1,m+1):
            if(m%j==0):
                ct+=1
        if(ct==2):
            break
    if((a-n)<(n-m)):
        return a
    elif((n-m)<(a-n)):
        return m
    else:
        return a,m
