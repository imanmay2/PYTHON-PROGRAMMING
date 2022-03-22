#A B C D E
#B C D E
#C D E
#D E
#E
#WAP to accept a string from the user and display the pattern shown above.
str1=input("Enter the string you want")
x=len(str1)
while(x>0):
    for i in str1:
        print(i,end=' ')
    print()
    str1=str1.replace(str1[0],'')
    x=x-1
    
        