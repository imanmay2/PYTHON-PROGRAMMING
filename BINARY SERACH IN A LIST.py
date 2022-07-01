li=eval(input("Enter the list you want"))
li.sort()
s=0
e=len(li)
key=int(input("Enter the element to be serached in the binary list"))
while(s<=e):
    mid=(s+e)//2
    if(li[mid]==key):
        print("ELEMENT FOUND AT A INDEX",mid)
        break
    elif(li[mid]>key):
        e=mid-1
    else:
        s=mid+1

    
