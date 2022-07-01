# dictionary S stores the roll no. and names of the students who have participated in the national league.
# print the roll number and names of those students who have participated.
S={}
n=int(input("how many students have participated"))
for i in range(n):
    r=int(input("enter the roll number of the students participated"))
    name=input("name of that very student")
    S[r]=name
print("The Dictionary created is")
print(S)
print("The Roll number of that students who have participated")
print(S.keys())
print("The names of that students who have participated")
print(S.values())
