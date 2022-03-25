str1=input("Enter the number like 123-456-7890")
li=str1.split('-')
if(len(li[0])==3 and len(li[1])==3 and len(li[2])==4):
    print("Yes!!!!You have entered the sequence of perfectly")
else:
    print("Nope!!!!You haven't entered the number in the correct order")



