import sys
x = 2
y = 3
z = 4


print(x**y)
print(17//4)

print((x<y<z) == (x<y and y<z))

print(int(True)) 

print(0b1001)
print(0o20)
print(0xFA)

print(oct(64))
print(bin(34))
print(hex(41))
print(int('65',8)) #Universal Converter to integer int('num',base)
print(int('1011',2)) #Universal Converter to integer         int('num',base)

print(repr('str'))
print(str('str'))
print('str')

sys.set_int_max_str_digits(0)  # 0 means no limit

# Calculate 2^1000
result = 2 ** 1000

# Print the result (this will be extremely large)
print(result)

import random

print(random.random)
print(random.randint(1,100))

arr=['pc','mobile','console','neither']

print(random.choice(arr))
random.shuffle(arr)
print(arr)

