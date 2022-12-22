#IMPLEMENTATION OF THE STACK OPERATION................

def isEmpty(stk):
    if(stk==[]):
        return True
    elif(stk!=[]):
        return False
def push(stk,item):
    item=int(input("Enter the item to be pushed in the stack: "))
    