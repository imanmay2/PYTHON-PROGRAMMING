
l=[i*2 for i in range(1,6)]
print(l)


li=["EV" if(i%2==0) else "odd" for i in range(10,20)]
print(li)




L=[("a",11),("b",12),("c",13)]
L1=[n*3 for (x,n) in L if x=="b" or x=="c"]
print(L1)
