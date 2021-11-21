# wap to read out the roll number and marks of n students and create a dictionary to print this.
n=int(input("enter the number of students input"))
d={}
for i in range(n):
    r,m=eval(input("enter the roll numbers, marks"))
    d[r]=m
print("Dictionary is as follows")
print(d)


# wap to modify the marks of the students by entering roll number from the user
print("Want to modify marks")
ans=input("enter yes/no").lower()
if(ans=="yes"):
    r1=int(input("enter roll number which you want to modify from the existing roll numbers"))
    if(r1 in d.keys()):
        d[r1]=float(input("enter the modified marks"))
        print("Modified Dictionary is as follows",d)
    else:
        print("No such roll numbers found")

        
# wap to input a roll number and delete it from the dictionary....
print("Want to delete any roll numbers from the list")
ans1=input("enter yes/no").lower()
if(ans1=="yes"):
    roll=int(input("enter the roll number to be deleted"))
    if(roll in d.keys()):
        del d[roll]
        print(roll,"has been successfully deleted from the dictionary")
        print("The updated dictionary is as follows")
        print(d)
    else:
        print("No such roll number found in the existing roll numbers")




