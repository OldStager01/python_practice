name="John Doe"
#Slicing
print(name[:])
print(name[0:4])
print(name[-3:])

#Upper & Lower
print(name.lower())
print(name.upper())

#Strip
name="   More Spaces  "
print(name)
print(name.strip())

#Replace
name="John Doe"
print(name.replace("John","Jane"))

#String to List
fruits="Mango, Banana, Jackfruit, Apple"
print(fruits.split(", "))

#List to String
fruits=["Mango", "Banana", "Jackfruit", "Apple"]
print(", ".join(fruits))

#Find
fruits="Mango, Banana, Jackfruit, Apple"
print(fruits.find("Banana"))
print(fruits.find("Kiwi"))

#Placeholders in print
chai="Masala"
quantity=3
print(f"I have ordered {quantity} of {chai} chai")
result="I have ordered {quantity} of {chai} chai"
print(result.format(quantity=quantity,chai=chai))

#Length
strPy="Why is 0.1 - 0.1 doesn't equals 0!?"
print(len(strPy))

#Iterate string
for letter in name:
    print(letter)

#Escape Sequence
strPy="He said,\"Python is easiest!\""
print(strPy)

strPy="c:\\sys32\\folder"
print(strPy)

#Don't ignore backslash
strPy=r"c:\sys32\folder" #r=Raw
print(strPy)

#Check if a string is present in string
strPy="He said,\"Python is easiest!\""
print("Python" in strPy)