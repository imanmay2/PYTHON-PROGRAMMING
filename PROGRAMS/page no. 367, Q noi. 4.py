phn=input("enter the phone number")
dig="0123456789"
ct=0
for i in phn:
    if(i in dig):
        ct+=1
if(ct==10):
    if(phn[3]=="-" and phn[7]=="-"):
        print("the legal input")
    else:
        print("not a legal input")
else:
    print("not a 10 digit phone number")
