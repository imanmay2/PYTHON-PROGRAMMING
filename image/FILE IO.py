# Write a function that reads a file and display the words separated with #
def hass():
    file=input("Enter the file name")
    with open(file) as f:
        li=f.read().split()
        for i in li:
            if(i!=li[len(li)-1]):
                print(i,end='#')
            else:
                print(i)
hass()        


