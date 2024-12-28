"""
1.1 CTCI : Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""
def isUnique(string):
    charset = [False for i in range(128)]
    for char in string:
        v = ord(char)#returns the ascii value of character
        if charset[v] == True:
            return False
        charset[v] = True
    return True
