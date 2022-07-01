line=input("enter the line")
lower=upper=digit=alpha=symbol=other=0
for a in line:
    if(a.islower()):
        lower=lower+1
    elif(a.isupper()):
        upper+=1
    elif(a.isdigit()):
        digit+=1
    elif(a.isalpha()):
        alpha+=1
    elif(a.isalnum()!=True and a!=' '):
        symbol+=1
    else:
        other+=1
print("the no. of uppercase letters are:",upper)
print("the no. of lowercase letters are:",lower)
print("the no. of alphabets letters are:",alpha)
print("the no. of digits letters are:",digit)
print("the no. of symbols are:",symbol)
print("the no. of others letters are:",other)
