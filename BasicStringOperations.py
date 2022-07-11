import ast


astring = "Hello world!"
bstring = 'Hello world!'

print("singlequotes are ' '")
#len prints length of string including punctuation and spaces.
print(len(astring))

# .index prints first occurance position value in string.
print(astring.index("o"))

# .count counts the amount in string
print(astring.count("l"))

# Prints the values of string between positions indicated.
print(astring[3:7]) # From index 3 to 7
print(astring[:7]) # From start to index 7
print(astring[3:-3]) # Negative numbers start at end and count back.
print(astring[3:7:2]) # From index 3 to 7 skipping 1

print(astring[::-1]) # Easy way to reverse a string
print(astring.upper()) # Converts to all uppercase
print(astring.lower()) # Converts to all lowercase

# True / False checks on a string
print(astring.startswith("Hello"))  
print(astring.endswith("asdfasdfasdf"))

# Splits a string on a delimiter as a list
afewwords = astring.split(" ") # splits up string on space delimiter
print(afewwords)