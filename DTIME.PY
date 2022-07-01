def time(t):
    if(t>=1200):
        d1=t-1200
    elif(t<1200):
        s=t//100
        l=t%100
        if(str(l)!='00'):
            l=60-l
            d1=int(str(12-(s+1))+str(l))
        else:
            d1=int(str(12-s)+l)
    return d1
def differ(t1,t2):
    if((t1<1200 and t2>=1200) or (t1>=1200 and t2<1200)):
        diff=time(t1)+time(t2)
        if(diff%100==60):
            diff=int(str((diff//100)+1)+str('00'))
        print('THE DIFFERECE BETWEEN THE TIMINGS IS AS FOLLOWS: ',diff//100,"HOURS",diff%100,"MINUTES")
    elif((t1<1200 and t2<1200) or (t1>=1200 and t2>=1200)):
        diff=time(t1)-time(t2)
        if(diff<0):
            diff*=(-1)
        if(diff%100==60):
            diff=int(str((diff//100)+1)+str('00'))
        print('THE DIFFERECE BETWEEN THE TIMINGS IS AS FOLLOWS: ',diff//100,"HOURS",diff%100,"MINUTES")


