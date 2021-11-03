l=[1,2,3,4,5,6,7,8,9,0,0,9,8,7,7,7,7,6,6,5,44,3,9,0,8]
c=0
n=int(input("enter the number to count how many times the number is present in the iven list"))
for i in l:
    if(i==n):
        c=c+1
print("the count of that number that you have entered is",c)
