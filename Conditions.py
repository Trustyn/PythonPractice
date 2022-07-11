x = 2
print(x == 2) # Prints out true
print(x == 3) # Prints out false
print(x < 3) # Prints out true

name = "Branden"
age = 36
if name == "Branden" and age == 36:
    print("Your name is %s, and you are %d years old." % (name, age))

if name == "Branden" or name == "Raven":
    print("Your name is either Branden or Raven.")

# in operator - used to check if a specified object exists within an iterable object container, like a list.
if name in ["Branden", "Raven"]:
    print("Your name is either Branden or Raven.")

Fstatement = False
Tstatement = True
if Fstatement is True:
    print("Statement 1")
    pass
elif Tstatement is True:
    print("Statement 2")
    pass
else:
    print("Statement 3")
    pass

if x == 2:
    print("x equals two!")
else:
    print("x does not equal two.")

# A statement is evaulated as true if one of the following is correct: 1. The "True" boolean variable is given, or calculated using an expression, such as an arithmetic comparison.
# 2. An object which is not considered "empty" is passed.
# Here are some examples for objects which are considered as empty: 1. An empty string: "" 2. An empty list: [] 3. The number zero: 0 4. The false boolean variable: False

# is operator - Compares the instances and not the values of variables
y = [1,2,3]
z = [1,2,3]
print(y == z) 
print(y is z)

# not operator - Placed before a boolean inverts the expression
print(not False)
print((not False) == (False))

