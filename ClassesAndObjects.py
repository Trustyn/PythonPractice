class Myclass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

#Object of the class which you can have multiple copies of
myobjectx = Myclass()
myobjecty = Myclass()

myobjecty.variable = "yackity"

#Accessing the object
print(myobjectx.variable)
print(myobjecty.variable)

#Accessing a function in a class
myobjectx.function() #Prints out the message

#__init__() function is a special function that is called when a function is being inititated.
# It's used for assigning values in a class.
class NumberHolder:
    def __init__(self, number):
        self.number = number

var = NumberHolder(7)
print(var.returnNumber()) #Prints 7        
