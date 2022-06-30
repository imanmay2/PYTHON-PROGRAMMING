def AMCount():
    f1=input("ENter any random file name you want")
    with open(f1,"w") as kh:
        str2=input("Enter the string you wanna enter")
        kh.write(str2)
    ct_m=ct_a=0
    with open(f1) as r:
        for i in r.read():
            if(i=="A" or i=="a"):
                ct_a+=1
            elif(i=="M" or i=="m"):
                ct_m+=1
        print("A or a: ",ct_a)
        print("M or m: ",ct_m)
AMCount()