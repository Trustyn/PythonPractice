# block_keyword block_name(argument1, argument2,...) Other block keywords if, for, while
def my_function():
    print("Hello from my function.")

def my_function_with_args(username, greeting):
    print("Hello, %s, From my function!, I wish you %s" %(username, greeting))

def sum_two_numbers(a, b):
    return a + b

#Calling functions
my_function() #Prints greeting
my_function_with_args("John Doe", "a great year!") #Prints with inserted arguments
x = sum_two_numbers(1,2) #x will be assigned value of 1 + 2


