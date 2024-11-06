def decimalBinary(num):
    str_=str()
    while(num!=0):
        rem=num%2
        str_+=str(rem)
        num=num//2
    return int(str_)

def binaryDecimal(num):
    str_=str(num)
    i=len(str_)-1
    res_=0
    while(i!=-1):
        res_+=int(str_[i])*(2**i)
        i-=1
    return res_

    
def complement(binNum):
    str_=str(binNum)
    newStr=str()
    for i in str_:
        if(i=="1"):
            newStr+="0"
        elif(i=="0"):
            newStr+="1"
    return int(newStr)

n=int(input(""))
if(n>=0 and n<109):
     print(binaryDecimal(complement(decimalBinary(n))))
else:
    print("Invalid")
    
