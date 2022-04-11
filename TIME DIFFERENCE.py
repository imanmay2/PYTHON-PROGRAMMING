t1=int(input("ENTER THE FIRST TIME : "))
t2=int(input("ENTER THE LAST TIME : "))
diff=((t1//100)*60+(t1%100))-((t2//100)*60+(t2%100))
if(diff<0):
    diff*=(-1)
print(diff//60," HOURS ",diff%60," MINS ")