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

#5. WAP to display output in tabular format
#   (as we see in MySQL output of select command) for inputs by user.
#6. WAP that will accept a CARBON CONTAINING COMPOUND and display the IUPAC NOMENCLATURE of that compound...
#   For e.g: C2H5OH as Ethanol
#   For e.g: CH4 as Methane