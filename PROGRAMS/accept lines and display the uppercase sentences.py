#Write a program to accept string/sentences from the
#user till the user enters “END” to. Save the data in a text
#file and then display only those sentences which begin
#with an uppercase alphabet.
with open("w.txt","w") as f:
    li=[]
    ans="y"
    while ans=="y":
        wr=input("enter the student")
        li.append(wr+"\n")
        ans=input("Wanna continue or enter end to end??")
    f.writelines(li)

with open("w.txt") as f1:
    k=f1.readlines()
    for i in k:
        if(i[0].isupper()):
            print(i)

    
    
    
    
