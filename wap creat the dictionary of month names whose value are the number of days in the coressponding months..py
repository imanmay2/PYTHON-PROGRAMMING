# 6. wap creat the dictionary of month names whose value are the number of days in the coressponding months.

month={"January":31,"February":28,"March":31,"April":30,"May":31,"June":30,"July":31,"August":31,"September":30,"October":31,"November":30,"December":31}

# a) Ask the user to enter the month and by using dictionary to tell how many days are in the same month..

m=input("Enter the month name").capitalize()
if(m in month.keys()):
    print("No. of days in",m,"is",month.get(m))
else:
    print("No such month!!!")

# b)print out all the keys in the alphabetical orders..

print("All the month name in the alphabetical order is as follows....")
print(sorted(month.keys()))

# c) print out all the months having 31 days.



