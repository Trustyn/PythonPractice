#Anagram is a word of phrase formed by rearranging the letters
#of a different word or phrase, typically using all the original
#letters exactly once.

#Given two strings s and t, return true if t is an anagram of
#s, and false otherwise.
#Example: s = "anagram", t = "nagaram" is True
#Example: s = "rat", t = "car" is False

def isAnagram(s, t):
    return sorted(s) == sorted(t)


s = "anagram"
t = "nagaram"
print(isAnagram(s,t))

s = "rat"
t = "car"
print(isAnagram(s,t))