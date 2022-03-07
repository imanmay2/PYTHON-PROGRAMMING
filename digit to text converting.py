d={1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",0:"Zero"}
n=int(input("Enter any number you want to enter"))
print("Alphabetically sequence is as follows.........")
li=[]
while(n!=0):
    r=n%10
    li.append(d[r])
    n=n//10
li=li[::-1]
for i in range(len(li)):
    print(li[i],end=' ')
