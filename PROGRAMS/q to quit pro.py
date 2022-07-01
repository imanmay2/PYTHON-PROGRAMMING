# repeatedly ask the user to input any sentence and change the uppercase to lowercase and vice versa.
while(1):
    str1=input("Enter the Sentence    ")
    s=''
    for i in str1:
        if(i.isupper()):
            s+=i.lower()
        elif(i.islower()):
            s+=i.upper()
        else:
            s+=i
    print(s)
    ans=input("Wanna Continue or enter q to quit    ")
    if(ans=='q'):
        break
    
