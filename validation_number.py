n=int(input(""))
li_=list()
for i in range(1,n+1):
    num=int(input(""))
    li_.append(num)

if(li_[0]>0):
    check="p"
elif(li_[0]<0):
    check="n"
f=0
for i in range(1,len(li_)-1):
    if(check=="p" and li_[i]<0):
        check="n"
    elif(check=="n" and li_[i]>0):
        check="p"
    else:
        f=1
        break
if(f==0):
    print("true")
elif(f==1):
    print("false")
