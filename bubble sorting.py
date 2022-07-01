#BUBBLE SORTING TECHNIQUE 1...
li=eval(input("enter the list you want to enter"))
for i in range(0,len(li)-1):
    for j in range(i+1,len(li)):
        if(li[i]>li[j]):
           (li[i],li[j])=(li[j],li[i])
print("List after sorting is as follows",li)

#BUBBLE SORTING TECHNIQUE 2.
ct=1
li=eval(input("Enter the list to be sorted"))
n=len(li)
while(ct<n):
    for i in range(0,n-ct):
        if(li[i]>li[i+1]):
            (li[i],li[i+1])=(li[i+1],li[i])
    ct+=1
print("The list after sorting is an follows",li)
        
