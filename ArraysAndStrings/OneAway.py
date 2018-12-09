"""
1.5: There are three types of edits that can be performed on strings: insert a character, remove a
character, or replace a character. Given two strings, write a function to check if they are one
edit(or zero) edits away.

example:
pale, ple -> True
pales, pale -> True
pale, bale -> True
pale, bake -> False
"""
def oneEditAway(first, second):
    if len(first) == len(second):
        return oneEditReplace(first, second)
    elif len(first) + 1 == len(second):
        return oneEditInsert(first, second)
    elif len(first) - 1 == len(second):
        return oneEditInsert(second, first)
    return False
def oneEditReplace(s1, s2):
    foundDifference = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if foundDifference:
                return False
            foundDifference = True
    return True

def oneEditInsert(s1, s2):
    index1, index2 = 0 , 0
    while(index1 < len(s1) and index2< len(s2)):
        if s1[index1] != s2[index2]:
            if index1 != index2:
                return False
            
