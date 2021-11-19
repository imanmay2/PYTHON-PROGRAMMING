# 3 . wap to convert a number entered by the user into its corresponding number in words.
word=["One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Zero"]
num=int(input("enter the number you want to enter"))
str1=str(num)
for i in str1:
    print(word[i+1],end=' ')
