month=input("enter the month of the year")
ct=0
month_li=["January","February","March","April","May","June","July","August","September","October","November","December"]
if(month in month_li):
    ct=(month_li.index(month))+1
    if(ct%2!=0):
        print(month,"ends with 31")
    elif(ct==8):
        print(month,"ends with 31")
    elif(month=="February"):
        year=int(input("enter the year as the end days of this month depends upon  leap year"))
        if(year%100==0 and year%400==0):
            print(month,"ends with 29")
        elif(year%100==0 and year%400!=0):
            print(month,"ends with 28")
        elif(year%4==0):
            print(month,"ends with 29")
        else:
            print(month,"ends with 28")
    elif(ct%2==0):
        print(month,"ends with 30")
else:
    print(month,"you have entered is a invalid one !!!! please enter a valid one????")
        
    
        
