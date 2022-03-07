month={"January":31,"February":28,"March":31,"April":30,"May":31,"June":30,"July":31,"August":31,"September":30,"October":31,"November":30,"December":31}
month_name=input("Enter the month name you wanna enter").capitalize()# 
if(month_name in month):
    print(month[month_name])
else:
    print("Invalid month name")


# print all month in alphabetical order.
print(sorted(month))

# print all the months having 31 as days.
for i in month:
    if(month[i]==31):
        print(i,end=' ')


