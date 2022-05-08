def find_fact(m):
    if(m==1):
        return 1
    else:
        return m* find_fact(m-1)
def find_power(x,y):
    if y==0:
        return 1
    else:
        return x*find_power(x,y-1)
def calculate(x,n):
    s=0
    a=0
    b=-1
    for i in range(n):
        a=a+2
        b=b+2
        s=s+(find_power(x,a)/find_fact(b))
    return s
def display():
    return s
x=int(input("ENTER YOUR DESIRED NUMBER: "))
n=int(input("ENTER THE NUMBER OF TERMS OF THE SERTIES: "))
display()


