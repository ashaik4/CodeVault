# flatten 2D arrays into a single array

A = [[1, 2, 3], [4], [5, 6]]
# iterative version

def flatten_iterative(A):
    result = []
    for array in A:
        for element in array:
            result.append(element)
    return result

print(flatten_iterative(A))

# recursively traverse 2 dimensional list out of order.
def traverse_list(A):
    result = []
    def traverse_list_rec(A, i, j):
        if i >= len(A) or j >= len(A[i]):
            return
        traverse_list_rec(A, i + 1, j)
        traverse_list_rec(A, i, j + 1)
        result.append(A[i][j])
    traverse_list_rec(A, 0, 0)
    return result

print(traverse_list(A))

# recursively traverse 2 dimensional list in order.
def flatten(A):
    result = []
    def flatten_recursive(A, i, j, result):
        if i == len(A):
            return
        if j == len(A[i]):
            flatten_recursive(A, i + 1, 0, result)
            return
        result.append(A[i][j])
        flatten_recursive(A, i, j + 1, result)

    flatten_recursive(A, 0, 0, result)
    return result

print(flatten(A))
