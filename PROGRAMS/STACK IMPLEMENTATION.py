def Push(stk,n):
    stk.append(n)


def Pop(stk):
    if(stk!=[]):
        i=stk.pop()
    else:
        return "Overflow"


def Peek(stk):
    if stk!=[]:
        return stk[len(stk)-1]
    else:
        return "Overflow"

def Display_stk(stk):
    if stk==[]:
        return "Overflow"
    else:
        for i in range(len(stk)-1,-1,-1):
            print(stk[i])

stk=list()
while True:
    print("WELCOME TO THE STACK OPERATION")
    print("______________________________")
    print("SELECT ANYONE ONE OF THE FOLLOWING")
    print("1. PUSH")
    print("2. POP")
    print("3. PEEK")
    print("4. DISPLAY")
    print("5. EXIT")
    ch=int(input("Enter your desired choice: "))
    if(ch==1):
        n=int(input("Enter the item to be inserted: "))
        Push(stk,n)
    elif(ch==2):
        Pop(stk)
    elif(ch==3):
        print("The Topmost element in the stack is : ",Peek(stk))
    elif(ch==4):
        Display_stk(stk)
    elif(ch==5):
        break
    else:
        print("INVALID CHOICE !!1 PLEASE SELECT FROM 1 TO 5!!")
