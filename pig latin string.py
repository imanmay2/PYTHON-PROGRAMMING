# pig latin string
str1=input("Enter any word you want")
print(str1[1:len(str1)+1])
print(str1[0])
s=str1[1:-1]+str1[0:1]+"ay"
print("PIG LATIN STRING IS AS FOLLOWS",s)