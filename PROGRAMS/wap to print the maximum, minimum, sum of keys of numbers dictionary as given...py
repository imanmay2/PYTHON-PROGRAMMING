#wap to print the maximum, minimum, sum of keys of numbers dictionary as given..
#       num={1:111,2:222,3:333,4:444}......Also find the maximum, minimum and sum of values.


num={1:111,2:222,3:333,4:444}
# key portion
print("Maximum among the keys is",max(num.keys()))
print("Miniimum among the keys is",min(num.keys()))
print("The sum of all the keys is",sum(num.keys()))

# value portion

print("Maximum among the values is",max(num.values()))
print("Miniimum among the values is",min(num.values()))
print("The sum of all the values is",sum(num.values()))
