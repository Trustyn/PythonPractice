#Dictionaries are similar to arrays but works with keys and values instead of indexes.
#Each value stored can be accessed using a key, which is a type of object(string, number, list, etc.).
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

#ALTERNATIVE INITIALIZATION
phonebook2 = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook2)

#Iterating over dictionaries
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

#Removing a value
del phonebook["John"]
print(phonebook)

#ALTERNATIVE REMOVAL OF VALUE
phonebook.pop("Jill")
print(phonebook)

#Adding a value
phonebook["Branden"] = 555990044
print(phonebook)

