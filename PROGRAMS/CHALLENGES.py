#1.Store userInp data other than  in a list and array.
def func1():
    inp=''
    ans='y'
    while(ans=='y'):
        item=input("Enter the item to be stored: ")
        inp=inp+item+','
        ans=input("Wanna store more datas?? y/n?? ")
    print("Datas which are stored is: ")
    for i in inp.split(','):
        print(i,end=',')


# WAP that will accept a person's age and check for its vote eligiblity.
# NOTE : USER CAN'T USE IF-ELSE STATEMENT FOR THE ABOV MENTIONED QUESTION.
def check_eligiblity():
    age=int(input("Enter the age"))
    while(age>18):
        print("PERSON IS ELIGIBLE FOR VOTE")
        break
    while(age<18):
        print("PERSON IS NOT ELIGIBLE FOR VOTE")
        print("HE WILL BE ELIGIBLE AFTER",18-age,"YEARS")
        break
#3. WAP to convert infix to postfix and reverse of it.
def infix_postfix(exp):
    op=['(',')','^','*','/','+','-']
    stk=list()
    output=''
    l=len(exp)
    ct=0
    for i in exp:
        ct+=1
        if(i.isalpha()):
            output=output+i
        elif(i in op):
            if(stk==[]):
                stk.append(i)
            elif(stk!=[]):
                top=stk[len(stk)-1]
                if(i=='*' and top=='/') or (i=='/' and top=='*') or (i=='+' and top=='-') or (i=='-' and top=='+'):
                    output+=top
                    stk.pop()
                    stk.append(i)
                elif(op.index(i)<=op.index(top)):
                    stk.append(i)
                elif(op.index(i)>op.index(top)):

                        while op.index(i)>=op.index(top):
                            output+=top
                            stk.pop()
                            
                            if(stk==[]):
                                stk.append(i)
                                
                                break
                            elif(op.index(i)<op.index(top)):
                                stk.append(i)
                                
                                break
                            top=stk[len(stk)-1]
                        
                elif(i=='^' and top=='^'):
                    stk.append(i)
                elif(i==')'):
                    if('(' not in stk):
                        #print("( not found in the expression")
                        break
                    else:
                        stk.append(')')
                        i1=stk.index('(')
                        i2=stk.index(')')
                        li=stk[i1+1:i2]
                        li=li[::-1]
                        for kj in li:
                            output+=kj
                        li=list()
        if(ct==l):
            stk=stk[::-1]
            for it in stk:
                output+=it



    return output 

              

#4. WAP to check precedence order of operators. Eg. Input => * and + … Output => * is in higher preceedance.
#   Eg: Input => * and / Output => Same preceedance …
def check_precedence(inp1,inp2):
    li_prece=['()','^','*','/','+','-']
    if(inp1=='*' and inp2=='/') or (inp1=='/' and inp2=='*') or (inp1=='+' and inp2=='-') or (inp1=='-' and inp2=='+'):
        print("Both ",inp1,'and',inp2,'are having same precedence')
    elif(li_prece.index(inp1)>li_prece.index(inp2)):
        print(inp1,"is in higher precedence")
    elif(li_prece.index(inp2)>li_prece.index(inp1)):
        print(inp1,"is in higher precedence")
    else:
        print("ERROR ENCOUNTERED!!!!!!")


#5. WAP that will accept a CARBON CONTAINING COMPOUND and display the IUPAC NOMENCLATURE of that compound...
#   For e.g: C2H5OH as Ethanol
#   For e.g: CH4 as Methane



#6.Wap that will accept a sentence and convert it in lower case except the text that it is given within quotes.
#   e.g- hello How Are 'YOU'.
# output-hello how are 'YOU'.
def func6(str1):
    return str1.split("'")[0].lower()+"'"+str1.split("'")[1]+"'"
print(func6('hello How Are "YOU"'))
