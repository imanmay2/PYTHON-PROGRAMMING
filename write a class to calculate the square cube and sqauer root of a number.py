n=int(input("enter the number you want to enter"))
class num:
    @staticmethod
    def greet():
        print("hello")
    def calculate(self,n):
        sq=n**2
        cub=n**3
        sq_root=n**0.5
        print("square of the number",n,"is",sq)
        print("cube of the number",n,"is",cub)
        print("square root of the number",n,"is",sq_root)
a=num()
a.greet()
a.calculate(n)


    
    
