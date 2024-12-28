def generate_combinations(N):
    return combinations(N, 0 )
def combinations(N, i ):
    toReturn = list()
    if i == len(N):
        toReturn.append(list())
        return toReturn
    else:
        subproblems = combinations(N, i + 1)
        for result in subproblems:
            toReturn.append(list(result))
            result.append(N[i])
            toReturn.append(list(result))
    return toReturn

N = [1,2,3,4,5]
combinations = generate_combinations(N)
for item in combinations:
    print(item)

# generate combinations in sorted order without using the sort() function
def generate_sorted_combinations(N):
    return sorted_combinations(N, len(N))
def sorted_combinations(N, i ):
    if i == 0:
        toReturn = list()
        toReturn.append(list())
        return toReturn
    toReturn = list()
    l = sorted_combinations(N, i - 1)
    for result in l:
        toReturn.append(list(result))
        result.append(N[i - 1])
        toReturn.append(list(result))
    return toReturn


sorted_combinations = generate_sorted_combinations(N)
for item in sorted_combinations:
    print(item)