#1WAP that prompts for a phone number of 10 digits and two dashes, with the dashes after the area code and the next three numbers.
# For e.g 017-555-1212 is a valid input.
str1=input("Enter the number")
if(str1[3]=='-' and str1[7]=='-' and len(str1[0:3])==3 and len(str1[4:7])==3 and len(str1[8:len(str1)])==4):
    print("VALID INPUT!!!!")
else:
    print("NOT A VALID INPUT!!!!")
