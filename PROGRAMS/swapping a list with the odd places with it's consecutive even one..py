#swapping a list with the odd places with it's consecutive even one.
li=eval(input("Enter the list"))
print("Original List entered by the user is",li)
if(len(li)%2!=0):
    print("PLEASE TRY WITH THE EVEN NUMBER OF LIST PLEASE!!!!")
else:
    for i in range(0,len(li),2):
        li[i],li[i+1]=li[i+1],li[i]
    print("The list now becomes after swapping is as follows")
    print(li)
        
        
    
