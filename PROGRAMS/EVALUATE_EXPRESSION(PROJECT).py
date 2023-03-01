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
        return True
    else:
        return False
def evaluate(exp):
    if(valid(exp)==False):
        print("INVALID EXPRESSION !! PLEASE ENTER A LEGITIMATE ONE!!")
    elif(valid(exp)==True):
        while True:
            s=str(exp)
            if(')' in s):
                st=s.index('(')
                end=s.index(')')
                sub=s[st+1:end+1]
                i=int(sub)