# wap that will print the following upto n terms
# a b ba bab ...n terms
def ask():
    global n
    n=int(input("ENTER THE RANGE OF THE FIBOSTRING SERIES: "))
def fibo_str():
    a='a'
    b='b'
    print("THE SERIES OF THE FIBOSTRING IS AS FOLLOWS: ",a,b,end=' ')
    for i in range(3,n+1):
        c=b+a
        print(c,end=' ')
        a=b
        b=c
ask()
fibo_str()