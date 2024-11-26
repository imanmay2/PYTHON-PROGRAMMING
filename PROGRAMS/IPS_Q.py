#     Write a program that will do the following task.
#     str1=ab#d
#     str2=ac#d       
#     Remove the # and the previous character, and check whether the strings are same or not.
#     If same , then return True, else False.


def convert_List(str1,str2):
    li1=list()
    li2=list()
    for i in str1:
        li1.append(i)
    for i in str2:
        li2.append(i)
    return (li1,li2)

def removehash(li):
    while('#' in li):
        idx=li.index("#")
        if(idx>0):
            li.pop(idx)
            li.pop(idx-1)
        else:
            li.pop(idx)
    return li



str1=input("Enter the String 1 : ")
str2=input("Enter the String 2 : ")


(li1,li2)=convert_List(str1,str2)
li1=removehash(li1)
li2=removehash(li2)
if(li1==li2):
    print(True)
else:
    print(False)