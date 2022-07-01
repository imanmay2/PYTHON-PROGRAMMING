class add:
    def sum(self):
        return self.a+self.b
num=add()
num.a=int(input("Enter the number"))
num.b=int(input("enter the number"))
s=num.sum()
print("Sum of the two numbers is",s)
