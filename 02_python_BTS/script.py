#Memory Reference
m = [1,2,3]
n = m
print(m == n) #!Checks Value (TRUE)
print(m is n) #!Checks if same memory reference (TRUE)

n = [1,2,3] #Init with same value as m
print(m == n) #!Checks Value (TRUE)
print(m is n) #!Checks if same memory reference (FALSE)

#To pass just the values instead of ref
a=['x','y','z']
b=a[:]
print(a==b) #!True
print (a is b) #!False

