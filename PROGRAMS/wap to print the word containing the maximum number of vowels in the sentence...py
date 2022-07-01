#wap to print the word containing the maximum number of vowels in the sentence..

str1=input("Enter the string")
ct=0
count=[]
li=str1.split()
for i in li:
    ct=0
    for j in i:
        if(j=="a" or j=="e" or j=="i" or j=="o" or j=="u" or j=="A" or j=="E" or j=="I" or j=="O" or j=="U"):
            ct=ct+1
    count.append(ct)

index_count=count.index(max(count))
print("The maximum number of vowels in the sentence is",li[index_count])


                                                                

            
        
