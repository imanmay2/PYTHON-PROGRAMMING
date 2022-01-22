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

#USING FUNCTION OF REVERSING OF A NUMBER.

def rev(n):
    reverse=0
    while(n!=0):
        r=n%10
        reverse=(reverse*10)+r
        n=n//10
    return reverse
def rev1(s):
    reverse1=0
    while(s!=0):
        r=s%10
        reverse1=(reverse1*10)+r
        s=s//10
    return reverse1

#inputing user's choice
ch=int(input("Enter you choice please"))
if(ch>=1 and ch<9):
    if(ch==1):
        deci=int(input("Enter the number you want"))
        str1=''
        while(deci!=0):
            r=deci%2
            str1=str1+str(r)
            deci=deci//2
        n=int(str1)
        print("BINARY CONVERSION IS",rev(n))
    elif(ch==2):
        bi=int(input("Enter any number you want"))
        k=0
        s=0
        while(bi!=0):
            r=bi%10
            s=s+(r*(2**k))
            k=k+1
            bi=bi//10
        print("DECIMAL CONVERSION IS",s)
    elif(ch==3):
        deci=int(input("Enter the number you want"))
        str2=''
        while(deci!=0):
            r=deci%8
            str2=str2+str(r)
            deci=deci//8
        n=int(str2)
        print("OCTAL CONVERSION IS",rev(n))
    elif(ch==4):
        oct=int(input("enter the number you want"))
        s=0
        k=0
        while(oct!=0):
            r=oct%10
            s=s+(r*(8**k))
            k=k+1
            oct=oct//10
        print("DECIMAL CONVERSION IS",s)
    elif(ch==5):
        oct=int(input("enter the number you want"))
        s=0
        k=0
        while(oct!=0):
            r=oct%10
            s=s+(r*(8**k))
            k=k+1
            oct=oct//10
        deci=s
        str1=''
        while(deci!=0):
            r=deci%2
            str1=str1+str(r)
            deci=deci//2
        n=int(str1)
        print("BINARY CONVERSION IS",rev(n))
    elif(ch==6):
        bi=int(input("Enter any number you want"))
        k=0
        s=0
        while(bi!=0):
            r=bi%10
            s=s+(r*(2**k))
            k=k+1
            bi=bi//10
        deci=s
        str2=''
        while(deci!=0):
            r=deci%8
            str2=str2+str(r)
            deci=deci//8
        n=int(str2)
        print("OCTAL CONVERSION IS",rev(n))
    elif(ch==7):
        deci=int(input("Enter the number you want"))
        li_3=[10,11,12,13,14,15]
        word="A B C D E F"
        li_4=word.split()
        print(li_4)
        str4=''
        while(deci!=0):
            r=deci%16
            if(r>9 and r<16):
                str4=str4+li_4[li_3.index(r)]
            else:
                str4=str4+str(r)
        deci=deci//16
        n=int(str4)
        print("HEXADECIMAL CONVERSION IS",rev(n))
        
        
        
