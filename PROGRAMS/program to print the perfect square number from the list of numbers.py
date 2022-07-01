#print the list of perfect square number from the list
li=[]
n=10
for i in range(n):
    num=int(input("Enter the number you want"))
    li.append(num)
for j in range(n):
    sq=li[j]**0.5
    num=int(li[j]**0.5)
    if(sq%num==0):
        print(li[j])

        
