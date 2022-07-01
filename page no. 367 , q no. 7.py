while(1):
    str1=input("enter the string or enter q or Q to quite")
    if(str1=="q" or str1=="Q"):
        break
    else:
        for i in str1:
            if(i.islower()):
                print(i.upper())
            elif(i.isupper()):
                print(i.lower())
