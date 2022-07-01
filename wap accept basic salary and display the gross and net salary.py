sal=float(input("enter your basic salary"))
da=0.1*sal
hra=0.12*sal
pf=0.075*sal
medi=0.08*sal
gs=sal+da+hra
ns=gs-pf
print("The gross salary is",gs)
print("The net salary is",ns)
