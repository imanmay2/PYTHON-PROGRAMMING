txt_list=open(input("Enter file name with extension and path: ")).read().split(' ')
temp,count_=0,txt_list.count(txt_list[0])
temp_list=[]
for i in range(len(txt_list)):
    if txt_list[i] in temp_list:
        continue
    temp=txt_list.count(txt_list[i])
    temp_list.append(txt_list[i]) if temp<=1 else None
print(temp_list)
