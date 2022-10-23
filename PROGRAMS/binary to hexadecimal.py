def bin_deci(bi):         #binary to decimal
    k=0
    s=0
    while(bi!=0):
            r=bi%10
            s=s+(r*(2**k))
            k=k+1
            bi=bi//10
    return s


def deci_hexa(deci):        # decimal to hexa decimal
    li_3=[10,11,12,13,14,15]
    word="A B C D E F"
    li_4=word.split()
    str4=''
    while(deci!=0):
        r=deci%16
        if(r>9 and r<16):
            str4=str4+li_4[li_3.index(r)]
        else:
            str4=str4+str(r)
        deci=deci//16
    return str4[::-1]



n=int(input("Enter the number"))
deci=bin_deci(n)
print("HEXADECIMAL CONVERSION IS",deci_hexa(deci))
