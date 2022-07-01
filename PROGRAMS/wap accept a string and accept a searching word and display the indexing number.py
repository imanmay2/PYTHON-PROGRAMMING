# wap accept a string and accept a searching word and display the indexing number
#where the word is in the string
str1=input("enter the string")
s=input("enter the searching element")
x=str1.find(s)
if(x>-1):
    print("the word's index is",x)
else:
    print("not present in the string")
