# WAP THAT WILL DISPLAY A RANDOM NUMBER WITHOUT USING/IMPORTING RANDOM MODULE/FUNCTION.
import time
t=time.time()
str1=str(t).split('.')[1]
l=str1[len(str1)-1]
print(str1[0:int(l)])
    
