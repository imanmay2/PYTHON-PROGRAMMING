#wap accept 10 elements in a tuple and display the perfect square root elements of the tuple
t=tuple()
n=tuple()
for i in range(1,11):
    num=int(input("enter"))
    n+=(num,)
print("original tuple",n)
for i in n:
    if((i**0.5)==int(i**0.5)):
        t+=((i),)
print("the tuple containing the tuple is",t)
