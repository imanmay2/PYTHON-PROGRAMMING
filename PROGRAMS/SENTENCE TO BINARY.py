# wap that will convert the sentence into it's binary format.
sent=input("Enter the string")
li_Bin=list()
Bin_add=bin(0)
for i in sent:
    li_Bin.append(bin(ord(i)))
print(li_Bin)
for i in li_Bin:
    Bin_add=Bin_add+(i)
print("DESIRED OUTPUT IS AS FOLLOWS: ",Bin_add)

