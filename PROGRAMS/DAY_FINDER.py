def day_finder(inp):# 13-April-2023 / 13-04-2023
    day=inp.split('-')[0]
    month=inp.split('-')[1]
    year=int(inp.split('-')[2])
    def leap_year(year):
        if(year%100==0 and year%400==0):
            return True
        elif(year%100==0 and year%400!=0):
            return False
        elif(year%4==0):
            return True
        else:
             return False
    def get_key(val):
        for key, value in d_week.items():
            if val == value:
                return key
 
        return "key doesn't exist"
    d_month_s={"january":1,"february":4,"march":4,"april":0,"may":2,"june":5,"july":0,"august":3,"september":6,"october":1,"november":4,"december":6}
    d_week={'sunday':0,'monday':1,'tuesday':2,'wednesday':3,'thrusday':4,'friday':5,'saturday':6}
    d_month_s={'01':1,"02":4,"03":4,"04":0,"05":2,"06":5,"07":0,"08":3,"09":6,"10":1,"11":4,"12":6}
    t_centuries=(6,4,2,0)
    if(type(month[0])==type('s')):
        cent=(int(year)//400)*400
        cent_p=int(year)%400
        # if((leap_year(year) is True) and (month=='01' or month=='02')):
        #     find=((int(day)+int(d_month_s[month])+cent+cent_p+(cent_p//4)-1)%7)-1
        if(leap_year is True):
            find=((int(day)+int(d_month_s[month])+cent+cent_p+(cent_p//4))%7)-1

    return get_key(find).capitalize()
inp=input("[*] ENTER THE DATE : ")
print(day_finder(inp))
