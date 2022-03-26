f=input("Enter the first day of the year").upper()
li=['SUNDAY','MONDAY','TUESDAY','WEDNESDAY','THRUSDAY','FRIDAY','SATURDAY']
n=int(input("Enter any day in-between 2-365"))
if(n<1 and n>365):
    print("INVALID DAY NUMBER!!!!PLEASE SELECT DAY IN-BETWEEN 2-365")
else:
    st=li.index(f)
    day=(n%7)+st-1
    if(day>=7):
        day=day-7
    print("DAY NUMBER OF",n,"IS",li[day])
