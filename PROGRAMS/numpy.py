import numpy as np
arr1=np.array([1,2,3,4])
arr2=np.array([1,2,3,5])
arr3=np.array([3.4,5,6,7])
print(arr1)
print(arr2)
print(np.equal(arr1,arr2))   #Checks equal arrays
print(np.all(arr1))
print(np.any(arr1))
print(np.less_equal(arr1,arr2))
print(np.isfinite(arr1))

x=np.ones(100)   #Generates 100 ones
print(x)


y=np.zeros(200)   #Generates 200 zeros
print(y)

print(np.ones(100)*22)

print(np.arange(1,100))  #Generates number from 1 to 99

print(np.arange(1,101).reshape(10,10))    #Converts 10X10 matrix ranging from 1-100

arr4=np.arange(1,101).reshape(10,10)
print(np.sum(arr4,axis=0))    # Sum of x-axis   #axis=1---y-axis

print(np.mean(arr4,axis=0))   # Mean of the first row of x axis.

arr5=np.array([1,2+2+0j,0+4j,3.14])
print(np.iscomplex(arr5))   # Checks only for the presence of imaginary number.
print(np.isreal(arr5))    #Checks for the real part only.
print(np.isscalar(arr5))   #Checks for the scaler value only.
