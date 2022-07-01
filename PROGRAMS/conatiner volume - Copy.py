def get_value():
    r=float(input("Enter the radius of the conatiner"))
    h=float(input("Enter the height of the conatiner"))
    type=input("Enter the type of the conatiner")
    return (r,h,type)
get_value()
def calVolume():
    if(type=="Cone"):
        v=(3.14*r*r*h)/3
    elif(type=="Cylinder"):
        v=(3.14*r*r*h)
    elif(type=="Hemisphere"):
        v=(2*3.14*r*r)/3
    elif(type=="Sphere"):
        v=(4*3.14*r*r)/3
def show_container():
    print(get_value())
    print("Volume of the container is: ",v)

calVolume()
show_container()
    



