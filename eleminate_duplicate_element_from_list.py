n=int(input(""))
list_=list()
list_non_duplicate=list()

def check_element(list_non_duplicate,num):
    for i in list_non_duplicate:
        if(i==num):
            return True
    return False

for i in range(0,n):
    list_.append(int(input("")))
list_non_duplicate[0]=list_[0]
for i in range(1,n):
    if(check_element(list_non_duplicate,list_[i])==False):
        list_non_duplicate.append(list_[i])
print(list_non_duplicate)