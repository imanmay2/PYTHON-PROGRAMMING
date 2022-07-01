n=int(input("enter the number for the multiplication table"))
def table(n):
    for i in range(1,11):
        print(n,"*",i,"=",n*i)
table(n)
