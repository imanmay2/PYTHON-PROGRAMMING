# WAP THAT WILL DISPLAY A RANDOM NUMBER WITHOUT USING/IMPORTING RANDOM MODULE/FUNCTION.
import time
n=input("Enter the starting range like: 0-8:::::")
s=int(str(n).split('-')[0])
e=int(str(n).split('-')[1])
while True:
    t=time.time()
    str1=str(t).split('.')[1]
    l=str1[len(str1)-1]
    res=int(str1[0:int(l)])
    if(res in range(s,e)):
        print(res)
        break
