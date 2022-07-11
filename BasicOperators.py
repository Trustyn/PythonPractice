import numbers


# Can use basic operators which also follows order of operations.
number = 1 + 2 * 3 / 4.0
print(number)

# Can use the modulo operator to return the remainder
remainder = 11 % 3
print(remainder)

# Can use ** to indicate "to the power"
squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

#Addition operator with strings to concatenate
helloworld = "hello" + " " + "world"
print(helloworld)

#Multiplication operator with strings to for a repeating sequence
lotsofhellos = "hello" * 10
print(lotsofhellos)

#Operators with lists
evenNumbers = [2,4,6,8]
oddNumbers = [1,3,5,7]
allNumbers = oddNumbers + evenNumbers
print(allNumbers)

#Form list and multiplication operator in 1 print
print([1,2,3] * 3)

