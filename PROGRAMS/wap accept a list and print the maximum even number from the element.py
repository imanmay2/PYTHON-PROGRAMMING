li=eval(input("enter the list"))
s1=0
ev=[]
s2=0
for i in li:
    if(i%2==0):
        ev.append(i)
if(len(ev)>0):
   print("maximum even is",max(ev))
else:
    print("even element is not present in the list")
