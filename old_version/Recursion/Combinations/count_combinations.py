N = [1,2,3,4,5]
def count_combinations(N):
    return count_combinations_rec(N, 0)
def count_combinations_rec(N, i ):
    if i == len(N):
        return 1
    exclude = count_combinations_rec(N, i+ 1)
    include = count_combinations_rec(N, i+ 1)
    return exclude + include
print(count_combinations(N))

### Write test cases


