def valid(exp):
    s=0
    s1=0
    s2=0
    for i in exp:
        if(i=='('):
            s+=1
        elif(i==')'):
            s-=1
        elif(i=='{'):
            s1+=1
        elif(i=='}'):
            s1-=1
        elif(i=='['):
            s2+=1
        elif(i==']'):
            s2-=1
    if(s1==s2==s==0):
        print("VALID EXPRESSION!!!!!")
    else:
        print("INVALID EXPRESSION!! PLEASE ENTER A VALID ONE!!!")
valid(input("ENTER THE EXPRESSION: "))