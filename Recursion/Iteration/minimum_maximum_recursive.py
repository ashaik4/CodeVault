import sys

# recursively find minimum and maximum of an array

def find_min(A):
    def find_min_recursive(A, i):
        if i <= 0:
            return A[i]
        return min(find_min_recursive(A, i-1), find_min_recursive(A, i-2))
    return find_min_recursive(A,len(A))

def find_max(A):
    result = 0
    def find_max_rec(A,i):
        if i<=0:
            return A[i]
        return max(find_max_rec(A, i - 1), find_max_rec(A, i - 2))
    result = find_max_rec(A, len(A))
    return result

A = [5,2,4,1]
print(find_min(A))
print(find_max(A))

# The above are bad solutions because time complexity is O(2**n)
# more elegant solution is:

def find_min_max(A):
    result = [sys.maxsize, -sys.maxsize]
    def min_max_recursive(A, i, result):
        if i >= len(A):
            return
        result[0] = min(A[0], A[i])
        result[1] = max(A[0], A[i])
        return min_max_recursive(A, i + 1, result)
    min_max_recursive(A, 0, result)
    return result

A = [5,2,4,1]
print(find_min_max(A))


