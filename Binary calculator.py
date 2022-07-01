#                       ....BINARY CALCULATOR...
print(".........WELCOME TO THE WORLD OF BINARY CALCULATOR............")
print("PLEASE SELECT ANY ONE OF THE FOLLOWING ONE")
print("1.  DECIMAL  TO BINARY")
print("2.  BINARY TO DECIMAL")
print("3.  DECIMAL TO OCTAL")
print("4.  OCTAL TO DECIMAL")
print("5.  OCTAL TO BINARY")
print("6.  BINARY TO OCTAL")
print("7.  DECIMAL TO HEXADECIMAL")
print("8.  HEXADECIMAL TO DECIMAL")
print("9.  BINARY TO HEXADECIMAL")
print("10. HEXADECIMAL TO BINARY")
print("11. HEXADECIMAL TO OCTAL")
print("12. OCTAL TO HEXADECIMAL")
print("13. EXIT")


def rev(n):
    reverse=0
    while(n!=0):
        r=n%10
        reverse=(reverse*10)+r
        n=n//10
    return reverse

def bin_deci(bi):         #binary to decimal
    k=0
    s=0
    while(bi!=0):
            r=bi%10
            s=s+(r*(2**k))
            k=k+1
            bi=bi//10
    return s
def deci_bin(deci):         # decimal to binary
    str1=''
    while(deci!=0):
            r=deci%2
            str1=str1+str(r)
            deci=deci//2
    n=int(str1)
    return rev(n)

def deci_oct(deci):      #decimal to octal
    str2=''
    while(deci!=0):
        r=deci%8
        str2=str2+str(r)
        deci=deci//8
    n=int(str2)
    return rev(n)
def oct_deci(oct):                 #octal to decimal
    s=0
    k=0
    while(oct!=0):
        r=oct%10
        s=s+(r*(8**k))
        k=k+1
        oct=oct//10
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
def hexa_deci(hexa):            #hexadecimal to decimal
    k=0
    s=0
    str1=str(hexa).upper()
    print(str1)

    he=int(str1)
    print(he)
    while(he!=0):
        r=he%10
        s=s+(r*(16**k))
        k=k+1
        he=he//10
    return s
while(1):
    ch=int(input("enter your choice please from the above menu"))
    if(ch>=1 and ch<12):
        if(ch==1):
            n=int(input("Enter the number"))
            print("BINARY CONVERSION IS",deci_bin(n))
        elif(ch==2):
            n=int(input("Enter any number"))
            print("DECIMAL CONVERSION IS",bin_deci(n))
        elif(ch==3):
            n=int(input("Enter the number"))
            print("OCTAL CONVERSION IS",deci_oct(n))
        elif(ch==4):
            n=int(input("enter the number"))
            print("DECIMAL CONVERSION IS",oct_deci(n))
        elif(ch==5):
            n=int(input("enter the number"))
            deci=oct_deci(n)
            print("BINARY CONVERSION IS",deci_bin(deci))
        elif(ch==6):
            n=int(input("Enter any number"))
            deci=bin_deci(n)
            print("OCTAL CONVERSION IS",deci_oct(deci))
        elif(ch==7):
            n=int(input("Enter the number"))
            print("HEXADECIMAL CONVERSION IS",deci_hexa(n))
        elif(ch==8):
            n=input("Enter the number")
            print("DECIMAL CONVERSION IS",hexa_deci(n))
        elif(ch==9):
            n=int(input("Enter the number"))
            deci=bin_deci(n)
            print("HEXADECIMAL CONVERSION IS",deci_hexa(deci))
        elif(ch==10):
            n=int(input("Enter any number"))
            deci=hexa_deci(n)
            print("BINARY CONVERSION IS",deci_bin(deci))
        elif(ch==11):
            n=int(input("Enter any number"))
            deci=hexa_deci(n)
            print("OCTAL CONVERSION IS",deci_oct(deci))
        elif(ch==12):
            n=int(input("Enter any number"))
            deci=oct_deci(n)
            print("HEXADECIMAL CONVERSION IS",deci_hexa(deci))
        else:
            break
    else:
        print("Please input in between 1 to 12")
        
        
        





    
    
    
    
    
