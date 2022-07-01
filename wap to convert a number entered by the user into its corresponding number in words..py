# 3 . wap to convert a number entered by the user into its corresponding number in words.
word={"1":"One","2":"Two","3":"Three","4":"Four","5":"Five","6":"Six","7":"Seven","8":"Eight","9":"Nine","0":"Zero"}
num=input("enter the number you want to enter")
for i in num:
    print(word[i],end=' ')

