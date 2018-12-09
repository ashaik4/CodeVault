"""
1.4: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase
that is the same backwards and forward.
"""
from collections import Counter
def permutation_of_palindrome(string):
    frequency_counter = Counter()
    string = string.replace(" ","")
    char_array = list(string)
    for i in char_array:
        frequency_counter[i] +=1
    flag = 0
    if len(string)%2 ==0:
        for key, value in frequency_counter.items():
            if value %2 !=0:
                return False
        return True
    else:
        for key, value in frequency_counter.items():
            if value%2 !=0 and flag == 0:
                flag = 1
            elif value%2 != 0 and flag:
                return False
        return True
print(permutation_of_palindrome("taco cat"))
print(permutation_of_palindrome(""))
print(permutation_of_palindrome("ARSHAD"))
print(permutation_of_palindrome("JAAJ"))
print(permutation_of_palindrome("echo"))


