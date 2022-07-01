def CI(p,t,r,nt):
    C=((p*(1+r/t))**nt)
    return C
p=float(input("enter the principal"))
nt=int(input("enter the number of times have you taken the interrest"))
r=float(input("enter the rate of interrest"))
t=int(input("enter the time"))
x=CI(p,t,r,nt)
print("the compund interest is as ",x)
