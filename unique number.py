


def equilateral_triangle(n):
    print("The equilateral triangle is as follows")
    for i in range(1,n+1,2):
        print(" "*n,"*"*i," "*n)
        n=n-1
n=int(input("enter the range of the equilateral triangle"))
equilateral_triangle(n)
