#REcord breaking data. 
# [1,2,0,7,2,0,2,2]

# conditions to be noted is that : 
# the number of visitors on that day is strictly larger than the number 
# of visitors on each of the previous days.
# Either it is the last day, or the number of visitors on the day is strictly larger than the number of visitors 
# on the following day.
# NOTE : every first day could be record breaking days.

def x_max(li,i):
    m1=0
    for j in range(0,i):
        m1=max(m1,li[j])
    return m1
li=eval(input("ENTER THE ELEMENTS : "))
ct=0
mx=max(li)
for i in range(0,len(li)-1):
    if(i==0 and li[i]>li[i+1]):
        print(li[i],"IS A RECORD BREAKING DAY. ")
        ct=1
    elif((i==len(li)-1) and (x_max(li,i)<li[i])):
        print(li[i],"IS A RECORD BREAKING DAY. ")
        ct=1
    elif(li[i]>x_max(li,i) and li[i]>li[i+1]):
        print(li[i],"IS A RECORD BREAKING DAY. ")
        ct=1
if(ct==0):
    print("NO RECORD BRAKING DAY IN THE GIVEN LIST.")
        
        
        
