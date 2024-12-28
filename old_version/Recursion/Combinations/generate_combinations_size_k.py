"""
Generate all combinations of size k
"""
"""bruteforce:"""

def generate_combinations(N):
    return combinations(N, 0 )
def combinations(N, i ):
    if i == len(N):
        toReturn = list()
        toReturn.append(list())
        return toReturn
    toReturn = list()
    for result in combinations(N, i + 1):
        toReturn.append(list(result))
        result.insert(0,N[i])
        toReturn.append(list(result))
    return toReturn

N = [1,2,3,4,5]
k = 2
combinations = generate_combinations(N)
for item in combinations:
    if len(item) == k:
        print(item)
"""optimization: backtrack"""
def generate_combinations(N, k):
    return combinations(N, 0 , k , 0)
def combinations(N, i, targetLength, currentLength ):
    if currentLength> targetLength:
        return list()
    if i == len(N) and targetLength!= currentLength:
        return list()
    if i == len(N):
        toReturn = list()
        toReturn.append(list())
        return toReturn

    included = combinations(N, i+1, targetLength, currentLength + 1)
    excluded = combinations(N, i+1 , targetLength, currentLength)
    toReturn = list()
    for result in included:
        result.insert(0,N[i])
        toReturn.append(list(result))
    toReturn+=excluded
    return toReturn

N = [1,2,3,4,5]
print(generate_combinations(N, 2 ))