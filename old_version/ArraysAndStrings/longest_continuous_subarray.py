""" Given an array of characters,  return an integer indicating the length of *continuous* subarray with max 2 distinct character

Input: ['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: the subarray ['C', 'A', 'C'] is the longest  continious subarrary with 2 distict charaters

Input: ['A', 'B', 'B', 'A', 'C', 'A', 'A', 'C', 'B']
Output: 5
Explanation: ['A', 'C', 'A', 'A', 'C']

Input: ['A', 'A', 'A']
Output: 3

Below is a bruteforce solution. Find a better one
"""
from collections import Counter


# Counter is a dictionary that returns count of a certain variable or character
def longest_continuous_array(A):
    def longest_continuous_array_util(A, i, j, longest,r):
        if i == len(A) or j == len(A):
            return
        subarray = A[i:j]
        # {'C':2, 'A': 1}
        distinct_chars_counter = Counter(subarray)
        if len(distinct_chars_counter.keys()) <= 2:
            r = max(longest, len(subarray))
            print(r)

        longest_continuous_array_util(A, i + 1, j, longest,r)
        longest_continuous_array_util(A, i, j + 1, longest,r)

    longest_len = -99999
    result_length = 0
    longest_continuous_array_util(A, 0, 0, longest_len,result_length)
    print(result_length)

A = ['A', 'B', 'B', 'A', 'C', 'A', 'A', 'C', 'B']
#A = ['A','B']
#print(longest_continuous_array(A))

def generate_combinations(N):
    m = -9999
    return combinations(N, 0, m)
def combinations(N, i , m):
    if i == len(N):
        toReturn = list()
        toReturn.append(list())
        return toReturn
    toReturn = list()
    for result in combinations(N, i + 1, m):
        toReturn.append(list(result))
        result.append(N[i])
        distinct_dict = Counter(result)
        if len(distinct_dict.keys()) <= 2:
            print(result)
            print(max(len(result), m))
            m = len(result)
        toReturn.append(list(result))
    return toReturn

A = ['A', 'B', 'B', 'A', 'C', 'A', 'A', 'C', 'B']
combos = generate_combinations(A)
# import pprint
# pprint.pprint(combos)
