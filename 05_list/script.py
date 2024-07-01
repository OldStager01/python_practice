tea_varieties = ['green', 'black', 'oolong', 'white']
print(tea_varieties)

print(tea_varieties[1:3])
print(tea_varieties[2:])
print(tea_varieties[1:1])

tea_varieties[1] = 'yellow' #Replaces the element at index 1
print(tea_varieties)

tea_varieties[1:2] = ['black','red'] #Inserts two elements at index 1
print(tea_varieties)

tea_varieties[1:1] = ['blue'] #Inserts one element at index 1
print(tea_varieties)

tea_varieties[1:3] = [] #Deletes two elements starting at index 1
print(tea_varieties)    

tea_varieties.append('green') #Appends an element to the end of the list
print(tea_varieties)

tea_varieties.insert(1,'black') #Inserts an element at index 1
print(tea_varieties)

tea_varieties.remove('black') #Removes the first occurrence of 'black'
print(tea_varieties)

tea_varieties.pop() #Removes the element
print(tea_varieties)

tea_varieties.pop(2) #Removes the element at index 2
print(tea_varieties)

#*Pop returns the element that was removed
#*Remove does not return the element that was removed

tea_varieties_copy=tea_varieties.copy();
print(tea_varieties_copy)

#!Loops

for tea in tea_varieties:
    print(tea,end="-")

print();

for tea in range(len(tea_varieties)):
    print(tea_varieties[tea],end="-")

if 'green' in tea_varieties:
    print('green is in the list')

squares_nums=(x**2 for x in range(5))
print(list(squares_nums))

cubed_nums=(x**3 for x in range(5))
print(list(cubed_nums))