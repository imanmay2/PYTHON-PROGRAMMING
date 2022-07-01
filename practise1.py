li=eval(input("Enter the list of numbers you wanna enter"))
print("Existing list is as follows",li)
n=eval(input("Enter the integer or list to be appended in the existing one"))
if(type(n)==type(1)):
    li.append(n)
elif(type(n)==type([])):
    li.extend(n)
else:
    print("You didn't enter neither integer nor list")
print("Updated list is as follows:   ",li)
