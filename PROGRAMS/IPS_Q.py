#     Write a program that will do the following task.
#     str1=ab#d
#     str2=ac#d       
#     Remove the # and the previous character, and check whether the strings are same or not.
#     If same , then return True, else False


def remove_hash(list_):
    ct=list_.count('#')
    while(ct>0):
        idx=list_.index('#')
        if(idx==0):
            list_.pop(idx)
        else:
            list_.pop(idx-1)
            list_.pop(idx)
        ct-=1
    return list_
        




str1=input("Enter the 1st String : ").split()
str2=input("Enter the 2nd String : ").split()
if(remove_hash(str1)==remove_hash(str2)):
    print("True")
else:
    print("False")  
