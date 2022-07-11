#Print with variables
name = "Branden"
age = 36
mylist = [1,2,3]
print("Hello, %s!" % name)
print("%s is %d years old." % (name, age))
print("A list: %s" % mylist)

# %s = String (or any object with a string representation, like numbers)
# %d = integers
# %f = floating point numbers
# %.<number of digits>f = Floating point numbers with a fixed amount of digits to the right of the dot
# %x/%X Integers in hex representation (lowercase / uppercase)

#Example 
data = ("John", "Doe", 53.44)
format_string = "Hello, %s %s. Your current balance is $%s."
print(format_string % data)
