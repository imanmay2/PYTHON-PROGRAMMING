def LShift(Arr,n):
    for i in range(0,len(Arr)-n):
        if i-n<0:
            pos=i-n+len(Arr)
        else:
            pos=i-n
        Arr[i],Arr[pos]=Arr[pos],Arr[i]
    print(Arr)
LShift([1,2,3,4,5,6],4)
